import importlib

from django.utils.translation import ugettext as _
from django.db import models
from model_utils import Choices
from autoslug import AutoSlugField
from positions import PositionField
from crispy_forms.helper import FormHelper
from crispy_forms import layout

import floppyforms as forms
import jsonfield

from formulator.conf import settings


class Form(models.Model):
    """
    Form class
    """

    ENCTYPES = Choices((0, 'urlencoded', 'application/x-www-form-urlencoded'),
                       (1, 'multipart', 'multipart/form-data'),
                       (2, 'plain', 'text/plain'))

    METHODS = Choices((0, 'get', 'GET'), (1, 'post', 'POST'))

    name = models.CharField(max_length=100, help_text='Name of the Form type')
    slug = AutoSlugField(unique=True, populate_from='name')  # will be used to autopopulate the ID

    # form attributes
    form_name = models.CharField(max_length=100, blank=True)
    form_action = models.CharField(max_length=250, blank=True)
    form_method = models.IntegerField(max_length=10, choices=METHODS, default=METHODS.get)

    form_accept_charset = models.CharField(max_length=100, blank=True)
    form_autocomplete = models.BooleanField(default=False)
    form_novalidate = models.BooleanField(default=False)
    form_enctype = models.IntegerField(choices=ENCTYPES, default=ENCTYPES.urlencoded)
    form_target = models.CharField(max_length=50, blank=True)

    # json field for global and event attributes, including class, id, etc...
    attrs = jsonfield.JSONField()

    def __unicode__(self):
        return u"formulator.Form instance: %s" % self.slug

    def save(self, *args, **kwargs):
        super(Form, self).save(*args, **kwargs)

    @property
    def fieldsets(self):
        return self.fieldset_set.all()

    def form_class_factory(self, form_class=None):
        # again make sure that we have everything we need to create a class
        self.full_clean()

        if form_class is None:
            form_class = forms.BaseForm

        attrs = {}
        fields = {}
        #fieldsets = []
        layouts = []

        for fieldset in self.fieldsets:
            fieldset_fields = fieldset.fields

            fieldset_layout = layout.Fieldset(fieldset.legend, *[f.name for f in fieldset_fields])
            layouts.append(fieldset_layout)

            for field in fieldset_fields:
                fields[field.name] = field.formfield_instance_factory()

        attrs['base_fields'] = fields

        helper = FormHelper()
        helper.layout = layout.Layout(*layouts)

        attrs['helper'] = helper

        return type(str(self.slug), (form_class,), attrs)


class FieldSet(models.Model):
    """
    """
    form = models.ForeignKey(Form)
    position = PositionField(collection='form')
    name = models.CharField(max_length=100)
    legend = models.CharField(max_length=100)

    @property
    def fields(self):
        return self.field_set.all()


class Field(models.Model):
    """
    """
    formset = models.ForeignKey(FieldSet)
    name = models.CharField(max_length=100, )
    position = PositionField(collection='formset')
    slug = AutoSlugField(unique=True, populate_from='name')

    field = models.CharField(max_length=100, choices=settings.FORMULATOR_FIELDS)
    widget = models.CharField(max_length=100, choices=settings.FORMULATOR_WIDGETS, blank=True,
                              help_text="""A Widget class, or instance of a Widget class, that should
                                           be used for this Field when displaying it. Each Field has a
                                           default Widget that it'll use if you don't specify this. In
                                           most cases, the default widget is TextInput.""")

    required = models.BooleanField(default=False, help_text=_('Boolean that specifies whether the field is required.'))
    label = models.CharField(max_length=100, blank=True,
                             help_text=_("""A verbose name for this field, for use in displaying this
                                            field in a form. By default, Django will use a "pretty"
                                            version of the form field name, if the Field is part of a
                                            Form. """))

    initial = models.CharField(max_length=200, blank=True,
                               help_text=_("""A value to use in this Field's initial display. This value
                                              is *not* used as a fallback if data isn't given. """))

    hidden = models.BooleanField(default=False, help_text=_('Boolean that specifies whether the field is hidden.'))
    help_text = models.TextField(blank=True, help_text=_("An optional string to use as 'help text' for this Field."))
    attrs = jsonfield.JSONField()

    def formfield_instance_factory(self, field_class=None, attrs=None):
        """Returns an instance of a form field"""

        if field_class is None:
            field_class = dict(settings.FORMULATOR_FIELDS)[self.field]

        module_name, class_name = field_class.rsplit(".", 1)
        module = importlib.import_module(module_name)
        field = getattr(module, class_name)
        attribs = { "position":self.position,
                    "required":self.required,
                    "hidden":self.hidden,
                    "attrs":self.attrs
                  }
        return type(str(self.label), (field,), attribs)

    def __unicode__(self):
        return u"Form instance: %s" % self.slug
