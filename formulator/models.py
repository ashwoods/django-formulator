from __future__ import unicode_literals

import re
import importlib

from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from model_utils import Choices
from collections import OrderedDict, Counter
from autoslug import AutoSlugField
from autoslug.settings import slugify as default_slugify
from positions import PositionField
from crispy_forms.helper import FormHelper
from crispy_forms import layout
from hvad.models import TranslatableModel, TranslatedFields

import floppyforms as forms
from django_hstore import hstore

from formulator.conf import settings


# Autoslugify modification to obtain slugs like valid variable names 
def variable_slugify(value):
    return default_slugify(value).replace('-', '_')


def create_field_slug(instance):
    return variable_slugify("%s %s" % (instance.fieldset.slug, instance.name))


@python_2_unicode_compatible
class Form(models.Model):
    """
    Model that defines a django Form class. The form_class_factory method returns a Form class with a default base of
    a floppy form Form class. It uses crispyforms helpers to add the additional form properties that django forms don't
    handle out of the box. It also uses crispyform fieldsets per default.
    """
    ENCTYPES = Choices((0, 'urlencoded', 'application/x-www-form-urlencoded'),
                       (1, 'multipart', 'multipart/form-data'),
                       (2, 'plain', 'text/plain'))

    METHODS = Choices((0, 'get', 'GET'), (1, 'post', 'POST'))

    name = models.CharField(max_length=100, help_text='Name of the Form type')

    # HTML5 FORM ATTRIBUTES for crispy forms

    # common form attributes
    form_name = models.CharField(max_length=100, blank=True)
    form_action = models.CharField(max_length=250, blank=True)
    form_method = models.IntegerField(max_length=10, choices=METHODS, default=METHODS.post)
    form_id = AutoSlugField(populate_from='name', unique=True, slugify=variable_slugify) 
    form_class = models.CharField(max_length=250, blank=True)

    # secondary attributes
    form_accept_charset = models.CharField(max_length=100, blank=True)
    form_autocomplete = models.BooleanField(default=False)
    form_novalidate = models.BooleanField(default=False)
    form_enctype = models.IntegerField(choices=ENCTYPES, default=ENCTYPES.urlencoded)
    form_target = models.CharField(max_length=50, blank=True)

    # json field for global and event attributes
    attrs = hstore.DictionaryField(null=True, blank=True)

    objects = hstore.HStoreManager()

    def __str__(self):
        return "formulator.Form instance: %s" % self.name

    def save(self, *args, **kwargs):
        super(Form, self).save(*args, **kwargs)

    @property
    def fieldsets(self):
        return self.fieldset_set.all()

    def form_class_factory(self, form_class=forms.Form):
        
        # again make sure that we have everything we need to create a class
        self.full_clean()

        helper = FormHelper()

        attrs = {}
        layouts = []
        
        # Checks for the existance of fields with repeat_min and/or repeat_max 
        # attributes.
        for fieldset in self.fieldsets:
            fieldset_fields = fieldset.fields

            fieldset_layout = layout.Fieldset(fieldset.safe_legend, *[f.field_id for f in fieldset_fields])
            layouts.append(fieldset_layout)

            for field in fieldset_fields:
                if field.repeat_max:
                    attrs[field.field_id + '_repeat_max'] = field.repeat_max
                if field.repeat_min > 1:
                    for i in range(0, field.repeat_min):
                        field_name = field.field_id + '_' + str(i) 
                        attrs[field_name] = field.formfield_instance_factory()
                else:
                    attrs[field.field_id] = field.formfield_instance_factory()

        helper.form_id = self.form_id
        helper.form_action = self.form_action
        helper.form_method = self.METHODS[self.form_method]
        helper.attrs = {
            'accept-charset': self.form_accept_charset,
            'autocomplete': self.form_autocomplete,
            'novalidate': self.form_novalidate,
            'enctype': self.form_enctype,
            'target': self.form_target
        }

        helper.layout = layout.Layout(*layouts)

        class MyForm(form_class):
            
            def __init__(self, *args, **kwargs):
                super(MyForm, self).__init__(*args, **kwargs)
                # Counter object with repeating field names, those matching the
                # regular expresion, and the times they occur in data.
                rep_fields = Counter([re.split('_\d+$', f)[0] for f in self.data.keys()])

                for f in rep_fields.keys():
                    rep_var = f + '_repeat_max'

                    if hasattr(self, rep_var):
                        maximum = getattr(self, rep_var)
                        provided = rep_fields.get(f)
                        # Counter object with existing field names and the times they occur
                        ex_fields = Counter([re.split('_\d+$', f)[0] for f in self.fields.keys()])

                        if provided > maximum:
                            # Create fields up to maximum 
                            for sub in range(ex_fields[f], maximum):
                                self.fields[f + '_' + str(sub)] = Field.objects.get(field_id=f).formfield_instance_factory()
                        else: 
                            # Create fields up to provided
                            for sub in range(ex_fields[f], provided):
                                self.fields[f + '_' + str(sub)] = Field.objects.get(field_id=f).formfield_instance_factory()

        attrs['helper'] = helper
        return type(str(self.form_id), (MyForm,), attrs)
        #return type(str(self.form_id), (form_class,), attrs)


@python_2_unicode_compatible
class FieldSet(TranslatableModel):
    form = models.ForeignKey(Form)
    position = PositionField(collection='form')
    name = models.CharField(max_length=100)
    slug = AutoSlugField(unique_with="form", populate_from='name', slugify=variable_slugify)

    @property
    def safe_legend(self):
        try:
            return self.legend
        except:
            return self.name.title()




    translations = TranslatedFields(
        legend=models.CharField(max_length=200),
    )

    class Meta:
        ordering = ['position']

    @property
    def fields(self):
        return self.field_set.all()

    def __str__(self):
        return "FieldSet: %s %s" % (self.name, self.form.name)


@python_2_unicode_compatible
class Field(TranslatableModel):
    """
    Stores the information for a django form field.

    """

    fieldset = models.ForeignKey(FieldSet)
    name = models.CharField(max_length=200,
                            help_text=_("""A short name to build the database field """))

    field_id = AutoSlugField(unique_with='fieldset__form', populate_from=create_field_slug, slugify=variable_slugify)
    position = PositionField(collection='fieldset')

    field = models.CharField(max_length=100, choices=settings.FORMULATOR_FIELDS)

    maxlength = models.IntegerField(blank=True, null=True)
    attrs = hstore.DictionaryField(blank=True, null=True)

    required = models.BooleanField(default=True,)
    widget = models.CharField(max_length=100, choices=settings.FORMULATOR_WIDGETS, blank=True,
                              help_text=_("""A Widget class, or instance of a Widget class, that should
                                           be used for this Field when displaying it. Each Field has a
                                           default Widget that it'll use if you don't specify this. In
                                           most cases, the default widget is TextInput."""))

    show_hidden_initial = models.BooleanField(
        default=False,
        help_text=_('Boolean that specifies whether the field is hidden.'))

    repeat_min = models.IntegerField(default=1,
                                     help_text=_("The minimum number of times this Field should appear in the Form"))

    repeat_max = models.IntegerField(blank=True,
                                     null=True,
                                     help_text=_("The maximum number of times this Field should appear in the Form"))

    translations = TranslatedFields(
        label=models.CharField(max_length=200,
                               help_text=_("""A verbose name for this field, for use in displaying this
                                            field in a form. By default, Django will use a "pretty"
                                            version of the form field name, if the Field is part of a
                                            Form. """)),
        help_text=models.TextField(blank=True,
                                   help_text=_("An optional string to use as 'help text' for this Field.")),

        initial=models.CharField(max_length=200, blank=True,
                                 help_text=_("""A value to use in this Field's initial display. This value
                                              is *not* used as a fallback if data isn't given. """)),

        choices=hstore.DictionaryField(blank=True, null=True),

    )

    @property
    def safe_label(self):
        try:
            return self.label
        except:
            return self.name.title()

    @property
    def safe_initial(self):
        try:
            return self.initial
        except:
            return ''

    @property
    def safe_help_text(self):
        try:
            return self.help_text
        except:
            return ''


    class Meta:
        ordering = ['position']

    def __str__(self):
        return "Field: %s" % self.name

    def formfield_instance_factory(self, field_class=None, attrs=None):
        """Returns an instance of a form field"""

        # Get the field class for this particular field
        if field_class is None:
            field_class = dict(settings.FORMULATOR_FIELDS)[self.field]


        module_name, class_name = field_class.rsplit(".", 1)
        module = importlib.import_module(module_name)
        field = getattr(module, class_name)


        # Get the widget class for this particular field
        if not self.widget:
            widget = getattr(field, 'widget', None)
        else:
            widget_class = dict(settings.FORMULATOR_WIDGETS)[self.widget]
            module_name, class_name = widget_class.rsplit(".", 1)
            module = importlib.import_module(module_name)
            widget = getattr(module, class_name)

        if attrs is None:
            attrs = {
                "required": self.required,
                "label": self.safe_label,
                "initial": self.safe_initial,
                "help_text": self.safe_help_text,
                "show_hidden_initial": self.show_hidden_initial,
            }

        if widget:
            attrs['widget'] = widget(attrs=self.attrs)

        try:
            choices = self.choices
        except:
            choices = None

        if choices:
            choices = [(key, _(value)) for key, value in choices.iteritems()]
            choices.reverse()
            attrs['choices'] = choices

        if self.maxlength:
            attrs['max_length'] = self.maxlength

        return field(**attrs)

    class Meta:
        ordering = ['position']


