# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import importlib

from django.utils.translation import ugettext_lazy as _
from django.db import models

from model_utils import Choices
from autoslug import AutoSlugField

from crispy_forms.helper import FormHelper
from crispy_forms import layout

from formulator.conf import settings

from .managers import FormQuerySet
from .utils import slugify, import_class


forms = importlib.import_module(settings.FORMULATOR_FIELDS_MODULE)
AbstractBaseModel = import_class(settings.FORMULATOR_ABSTRACT_BASE_MODEL)


class Form(AbstractBaseModel):
    """
    Stores HTML Form Attributes. Provides a factory method `form_factory` that
    returns a Django Form class by default.
    """

    ENCTYPES = Choices((0, 'URLENCODED', 'application/x-www-form-urlencoded'),
                       (1, 'MULTIPART', 'multipart/form-data'),
                       (2, 'PLAIN', 'text/plain'))

    METHODS = Choices((0, 'GET', 'GET'), (1, 'POST', 'POST'))

    name = models.CharField(max_length=100, help_text='Name of the Form type')

    # common HTML form attributes
    form_name = models.CharField(max_length=100, blank=True)
    form_action = models.CharField(max_length=250, blank=True)
    form_method = models.IntegerField(choices=METHODS, default=METHODS.POST)
    form_id = AutoSlugField(populate_from='name', slugify=slugify)
    form_class = models.CharField(max_length=250, blank=True)

    form_accept_charset = models.CharField(max_length=100, blank=True)
    form_autocomplete = models.BooleanField(default=False)
    form_novalidate = models.BooleanField(default=False)
    form_enctype = models.IntegerField(choices=ENCTYPES, default=ENCTYPES.URLENCODED)
    form_target = models.CharField(max_length=50, blank=True)

    objects = FormQuerySet.as_manager()

    def form_factory(self, form_class=None, attrs=None):
        """
        Returns a django Form class or of type `form_class`.


        :param form_class: Base class for the factory
        :param attrs: Extra runtime class attributes
        :return: Class of type `form_id`
        """
        if attrs is None:
            attrs = {}
        if form_class is None:
            form_class = import_class(settings.FORMULATOR_FORM_CLASS)

        # again make sure that we have everything we need to create a class
        self.full_clean()

        for field in self.fields.all():
            attrs[field.field_id] = field.field_factory()

        # set choices
        for choice in Choice.objects.all():
            if choice.field in self.field_set.all():
                attrs[choice.field.field_id].choices.append((choice.key, choice.value))

        layouts = []

        for fieldset in self.fieldsets.all():
            fieldset_layout = layout.Fieldset(
                fieldset.name,
                *[f.field_id for f in fieldset.fields])
            layouts.append(fieldset_layout)
            for field in fieldset.fields:
                attrs[field.field_id] = field.formfield_instance_factory()

        helper = getattr(form_class, 'helper', FormHelper())
        helper.form_id = self.form_id
        helper.form_action = self.form_action
        helper.form_method = self.METHODS[self.form_method]
        helper.attrs = {
            'accept-charset': self.form_accept_charset,
            'autocomplete': self.form_autocomplete,
            'novalidate': self.form_novalidate,
            'enctype': self.self.get_form_enctype_display(),
            'target': self.form_target,
        }
        helper.attrs = {k:v for k,v in helper.attrs if v}
        helper.layout = layout.Layout(*layouts)
        attrs['helper'] = helper

        return type(str(self.form_id), (form_class,), attrs)


class FieldSet(AbstractBaseModel):
    form = models.ForeignKey(Form, related_name='fieldsets')
    position = models.PositiveIntegerField(default=0, db_index=True)
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['form', 'position']
        unique_together = [('form', 'position'), ('form', 'name')]


class Field(AbstractBaseModel):
    """
    Stores the information for a django form field.

    """

    form = models.ForeignKey(Form, related_name='fields')
    position = models.PositiveIntegerField(default=0, db_index=True)
    fieldset = models.ForeignKey(FieldSet, null=True, related_name='fields')
    name = models.CharField(
        max_length=200,
        help_text=_("Verbose field name and form label ")
    )
    field_id = AutoSlugField(unique_with='form', populate_from='name', slugify=slugify)
    field_type = models.CharField(max_length=100, choices=settings.FORMULATOR_FIELDS)

    max_length = models.IntegerField(blank=True, null=True)
    placeholder = models.CharField(max_length=255, blank=True)
    required = models.BooleanField(default=True)
    help_text = models.TextField(
        blank=True,
        help_text=_("An optional string to use as 'help text' for this Field.")
    )
    initial = models.CharField(
        max_length=200,
        blank=True,
        help_text=_("Form field initial attribute")
    )
    widget = models.CharField(
        max_length=100,
        choices=settings.FORMULATOR_WIDGETS,
        blank=True,
        help_text=_("Widget class")
    )
    is_hidden = models.BooleanField(
        default=False,
        help_text=_('If the field is hidden.'))

    class Meta:
        ordering = ['form', 'position']
        unique_together = [('field_id', 'form'), ('field_id', 'fieldset')]

    def field_factory(self, field_class=None, field_attrs=None, widget_attrs=None):
        """Returns an instance of a form field"""

        if field_class is None:
            field_class = self.field_type

        if field_attrs is None:
            field_attrs = dict(self.fieldattributes.values_list('key', 'value'))

        if widget_attrs is None:
            widget_attrs = dict(self.widgetattributes.values_list('key', 'value'))

        field = import_class(field_class)

        if not self.widget:
            widget = getattr(field, 'widget', None)
        else:
            widget = import_class(self.widget)
        if widget:
            field_attrs['widget'] = widget(attrs=widget_attrs)

        field_attrs.update({
            'required': self.required,
            'label': self.name,
            'initial': self.initial,
            'help_text': self.help_text,
            'show_hidden_initial': self.show_hidden_initial,
            'max_length': self.max_length,
            'placeholder': self.placeholder,
        })

        return field(**field_attrs)


class FieldAttribute(AbstractBaseModel):
    field = models.ForeignKey(Field, related_name='field_attributes')
    key = models.CharField(max_length=100)
    value = models.CharField(max_length=100, blank=True)

    class Meta:
        unique_together = ('field', 'key')


class WidgetAttribute(AbstractBaseModel):
    field = models.ForeignKey(Field, related_name='widget_attributes')
    key = models.CharField(max_length=100)
    value = models.CharField(max_length=100)

    class Meta:
        unique_together = ('field', 'key')


class Choice(AbstractBaseModel):
    field = models.ForeignKey(Field, related_name='choices')
    position = models.PositiveIntegerField(default=0, db_index=True)
    key = models.CharField(max_length=100)
    value = models.CharField(max_length=100, blank=True)

    class Meta:
        ordering = ['field', 'position']
