from __future__ import unicode_literals

import importlib

from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.utils.functional import cached_property

from model_utils import Choices
from autoslug import AutoSlugField

from formulator.conf import settings


if settings.FORMULATOR_CRISPY_ENABLED:
    from crispy_forms.helper import FormHelper
    from crispy_forms import layout


class Form(settings.FORMULATOR_BASE_MODEL):

    ENCTYPES = Choices((0, 'urlencoded', 'application/x-www-form-urlencoded'),
                       (1, 'multipart', 'multipart/form-data'),
                       (2, 'plain', 'text/plain'))

    METHODS = Choices((0, 'get', 'GET'), (1, 'post', 'POST'))

    name = models.CharField(max_length=100, help_text='Name of the Form type')

    # common HTML form attributes
    form_name = models.CharField(max_length=100, blank=True)
    form_action = models.CharField(max_length=250, blank=True)
    form_method = models.IntegerField(choices=METHODS, default=METHODS.post)
    form_id = AutoSlugField(populate_from='name')
    form_class = models.CharField(max_length=250, blank=True)

    form_accept_charset = models.CharField(max_length=100, blank=True)
    form_autocomplete = models.BooleanField(default=False)
    form_novalidate = models.BooleanField(default=False)
    form_enctype = models.IntegerField(choices=ENCTYPES, default=ENCTYPES.urlencoded)
    form_target = models.CharField(max_length=50, blank=True)

    @cached_property
    def fieldsets(self):
        return self.fieldset_set.all().prefetch_related('field_set')

    def form_class_factory(self, form_class=None, attrs=None):
        if attrs is None:
            attrs = {}
        if form_class is None:
            form_class = settings.FORMULATOR_DEFAULT_FORM_CLASS

        # again make sure that we have everything we need to create a class
        self.full_clean()

        for field in self.field_set.all():
            attrs[field.field_id] = field.formfield_instance_factory()

        if settings.FORMULATOR_CRISPY_ENABLED:

            layouts = []

            for fieldset in self.fieldsets:
                fieldset_fields = fieldset.fields

                fieldset_layout = layout.Fieldset(fieldset.safe_legend, *[f.field_id for f in fieldset_fields])
                layouts.append(fieldset_layout)

                for field in fieldset_fields:
                    attrs[field.field_id] = field.formfield_instance_factory()

            helper = getattr(form_class, 'helper', FormHelper())
            helper.form_id = self.form_id
            helper.form_action = self.form_action
            helper.form_method = self.METHODS[self.form_method]
            helper.attrs = {}

            if self.form_accept_charset:
                helper.attrs['accept-charset'] = self.form_accept_charset
            if self.form_autocomplete:
                helper.attrs['autocomplete'] = self.form_autocomplete
            if self.form_novalidate:
                helper.attrs['novalidate'] = self.form_novalidate
            if self.form_enctype:
                helper.attrs['enctype'] = self.form_enctype
            if self.form_target:
                helper.attrs['target'] = self.form_target

            helper.layout = layout.Layout(*layouts)

            attrs['helper'] = helper

        return type(str(self.form_id), (form_class,), attrs)


class FieldSet(settings.FORMULATOR_BASE_MODEL):
    form = models.ForeignKey(Form)
    position = models.PositiveIntegerField(default=0, db_index=True)
    name = models.CharField(max_length=100)
    legend = models.CharField(max_length=200)

    @cached_property
    def safe_legend(self):
        try:
            return self.legend
        except:
            return self.name.title()

    @cached_property
    def fields(self):
        return self.field_set.all()

    class Meta:
        ordering = ['form', 'position']
        unique_together = ['form', 'position']


class Field(settings.FORMULATOR_BASE_MODEL):
    """
    Stores the information for a django form field.

    """

    form = models.ForeignKey(Form)
    position = models.PositiveIntegerField(default=0, db_index=True)
    fieldset = models.ForeignKey(FieldSet, null=True)
    label = models.CharField(max_length=200,
                             help_text=_("""A verbose name for this field, for use in displaying this
                                        field in a form. By default, Django will use a "pretty"
                                        version of the form field name, if the Field is part of a
                                        Form. """))

    name = models.CharField(max_length=200,
                            help_text=_("""A short name to build the database field """))

    field_id = AutoSlugField(unique_with='form', populate_from='name')

    field_type = models.CharField(max_length=100, choices=settings.FORMULATOR_FIELDS)

    # exceptions
    max_length = models.IntegerField(blank=True, null=True)
    placeholder = models.CharField(max_length=255, blank=True)

    required = models.BooleanField(default=True)
    help_text = models.TextField(blank=True,
                                 help_text=_("An optional string to use as 'help text' for this Field."))

    initial = models.CharField(max_length=200, blank=True,
                               help_text=_("""A value to use in this Field's initial display. This value
                                          is *not* used as a fallback if data isn't given. """))

    widget = models.CharField(max_length=100, choices=settings.FORMULATOR_WIDGETS, blank=True,
                              help_text=_("""A Widget class, or instance of a Widget class, that should
                                           be used for this Field when displaying it. Each Field has a
                                           default Widget that it'll use if you don't specify this. In
                                           most cases, the default widget is TextInput."""))

    show_hidden_initial = models.BooleanField(
        default=False,
        help_text=_('Boolean that specifies whether the field is hidden.'))


    class Meta:
        ordering = ['form', 'position']
        unique_together = ['form', 'position']

    def formfield_instance_factory(self, field_class=None, field_attrs=None, widget_attrs=None):
        """Returns an instance of a form field"""

        # Get the field class for this particular field
        # if field_class is None:
        #     for cls, n in settings.FORMULATOR_FIELDS:
        #         if n == self.field_type:
        #             field_class = cls
        if field_class is None:
            field_class = self.field_type

        if field_attrs is None:
            field_attrs = dict(self.fieldattribute_set.values_list('key', 'value'))

        if widget_attrs is None:
            widget_attrs = dict(self.widgetattribute_set.values_list('key', 'value'))

        module_name, class_name = field_class.rsplit(".", 1)
        module = importlib.import_module(module_name)
        field = getattr(module, class_name)

        # Get the widget class for this particular field
        if not self.widget:
            widget = getattr(field, 'widget', None)
        else:
            module_name, class_name = self.widget.rsplit(".", 1)
            module = importlib.import_module(module_name)
            widget = getattr(module, class_name)



        field_attrs.update({
            'required': self.required,
            'label': self.label,
            'initial': self.initial,
            'help_text': self.help_text,
            'show_hidden_initial': self.show_hidden_initial,
        })

        if self.max_length:
            widget_attrs['max_length'] = self.max_length

        if self.placeholder:
            widget_attrs['placeholder'] = self.placeholder

        if widget:
            field_attrs['widget'] = widget(attrs=widget_attrs)


        return field(**field_attrs)




class FieldAttribute(settings.FORMULATOR_BASE_MODEL):
    field = models.ForeignKey(Field)
    key = models.CharField(max_length=100)
    value = models.CharField(max_length=100, blank=True)


class WidgetAttribute(settings.FORMULATOR_BASE_MODEL):
    field = models.ForeignKey(Field)
    key = models.CharField(max_length=100)
    value = models.CharField(max_length=100)


class Choices(settings.FORMULATOR_BASE_MODEL):
    field = models.ForeignKey(Field)
    key = models.CharField(max_length=100)
    value = models.CharField(max_length=100, blank=True)
