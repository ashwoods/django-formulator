
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
import importlib

from django.utils.translation import ugettext as _
from collections import OrderedDict

from django.db import models
from model_utils import Choices
from autoslug import AutoSlugField
from positions import PositionField
from crispy_forms.helper import FormHelper
from crispy_forms import layout


import floppyforms as forms
from django_hstore import hstore

from formulator.conf import settings

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
    form_method = models.IntegerField(max_length=10, choices=METHODS, default=METHODS.get)
    form_id = AutoSlugField(populate_from='name', unique=True) 
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

        attrs = {}
        #fields = OrderedDict()
        layouts = []

        for fieldset in self.fieldsets:
            fieldset_fields = fieldset.fields

            fieldset_layout = layout.Fieldset(fieldset.legend, *[f.name for f in fieldset_fields])
            layouts.append(fieldset_layout)

            for field in fieldset_fields:
                attrs[field.name] = field.formfield_instance_factory()

        helper = FormHelper()

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

        attrs['helper'] = helper
        return type(str(self.form_id), (form_class,), attrs)


@python_2_unicode_compatible
class FieldSet(models.Model):
    form = models.ForeignKey(Form)
    position = PositionField(collection='form')
    name = models.CharField(max_length=100)
    legend = models.CharField(max_length=100)

    @property
    def fields(self):
        return self.field_set.all()

    def __str__(self):
        return "FieldSet %s with legend '%s' in form %s" % (self.name, self.legend, self.form.name)


@python_2_unicode_compatible
class Field(models.Model):
    """
    Stores the information for a django form field.

    """

    formset = models.ForeignKey(FieldSet)
    name = models.CharField(max_length=100, )
    position = PositionField(collection='formset')

    field = models.CharField(max_length=100, choices=settings.FORMULATOR_FIELDS)
    attrs = hstore.DictionaryField(blank=True, null=True)
    slug = AutoSlugField(unique=True, populate_from='name')

    required = models.BooleanField(default=True,
                                   help_text=_('Boolean that specifies whether the field is required.'))
    widget = models.CharField(max_length=100, choices=settings.FORMULATOR_WIDGETS, blank=True,
                              help_text=_("""A Widget class, or instance of a Widget class, that should
                                           be used for this Field when displaying it. Each Field has a
                                           default Widget that it'll use if you don't specify this. In
                                           most cases, the default widget is TextInput."""))

    label = models.CharField(max_length=100, blank=True,
                             help_text=_("""A verbose name for this field, for use in displaying this
                                            field in a form. By default, Django will use a "pretty"
                                            version of the form field name, if the Field is part of a
                                            Form. """))

    initial = models.CharField(max_length=200, blank=True,
                               help_text=_("""A value to use in this Field's initial display. This value
                                              is *not* used as a fallback if data isn't given. """))

    help_text = models.TextField(blank=True,
                                 help_text=_("An optional string to use as 'help text' for this Field."))

    show_hidden_initial = models.BooleanField(
        default=False,
        help_text=_('Boolean that specifies whether the field is hidden.'))

    def __str__(self):
        return "Field instance: %s" % self.name

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
            widget = field.widget
        else:
            widget_class = dict(settings.FORMULATOR_WIDGETS)[self.widget]
            module_name, class_name = widget_class.rsplit(".", 1)
            module = importlib.import_module(module_name)
            widget = getattr(module, class_name)

        # If label is left blank, create from field name
        if not self.label:
            label = self.name.title()
        else:
            label = self.label

        if attrs is None:
            attrs = {
                "required": self.required,
                "widget": widget(attrs=self.attrs),
                "label": label,
                "initial": self.initial,
                "help_text":self.help_text,
                "show_hidden_initial": self.show_hidden_initial,
            }

        return field(**attrs)

    class Meta:
        ordering = ['position']
