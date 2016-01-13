# -*- coding: utf-8 -*-
"""
Formulator Tests
"""

from django.core.exceptions import ValidationError
from django import forms

import floppyforms as floppy_forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset

base_fields = (
    'Field', 'CharField', 'IntegerField', 'DateField', 'TimeField',
    'DateTimeField', 'EmailField', 'FileField', 'ImageField', 'URLField',
    'BooleanField', 'NullBooleanField', 'ChoiceField', 'MultipleChoiceField',
    'FloatField', 'DecimalField', 'SlugField', 'GenericIPAddressField', 'TypedChoiceField',
    'TypedMultipleChoiceField', 'ComboField', 'MultiValueField',
    'SplitDateTimeField',
)

complex_fields = ('RegexField', 'FilePathField')


class BaseForm(object):

    FORM_CLASS = None

    def clean_honeypot(self):
        if self.cleaned_data.get('honeypot'):
            raise ValidationError('Haha, you trapped into the honeypot.')
        return self.cleaned_data['honeypot']

    def clean(self):
        if self.errors:
            raise ValidationError('Please correct the errors below.')


class DjangoTestForm(BaseForm, forms.Form):
    FORM_CLASS = forms

    honeypot = forms.CharField(required=False, widget=forms.HiddenInput)
    firstname = forms.CharField(label='Your first name?', required=True)
    lastname = forms.CharField(label='Your last name:')
    username = forms.CharField(widget=forms.TextInput(attrs={'max_length': 30, 'placeholder': 'username here'}))
    password = forms.CharField(
        widget=forms.PasswordInput,
        help_text='Make sure to use a secure password.',
    )
    password2 = forms.CharField(label='Retype password', widget=forms.PasswordInput)
    age = forms.IntegerField(required=False)

    def __init__(self, *args, **kwargs):

        super(FloppyTestForm, self).__init__(*args, **kwargs)
        for field in base_fields:
            self.fields[field.lower()] = getattr(self.FORM_CLASS, field)(label=field.title(), required=False)


class FloppyTestForm(BaseForm, floppy_forms.Form):
    FORM_CLASS = floppy_forms

    honeypot = FORM_CLASS.CharField(required=False, widget=FORM_CLASS.HiddenInput)
    firstname = FORM_CLASS.CharField(label='Your first name?', required=True)
    lastname = FORM_CLASS.CharField(label='Your last name:')
    username = FORM_CLASS.CharField(label='Username:', widget=FORM_CLASS.TextInput(attrs={'max_length': 30,
                                                                                          'placeholder': 'username here'
                                                                                          }))
    password = FORM_CLASS.CharField(
        widget=FORM_CLASS.PasswordInput,
        help_text='Make sure to use a secure password.'
    )
    password2 = FORM_CLASS.CharField(label='Retype password', widget=FORM_CLASS.PasswordInput)
    age = FORM_CLASS.IntegerField(label='Age', required=False)

    def __init__(self, *args, **kwargs):

        super(FloppyTestForm, self).__init__(*args, **kwargs)
        for field in base_fields:
            self.fields[field.lower()] = getattr(self.FORM_CLASS, field)(label=field.title(), required=False)

        self.fields['choicefield'].choices = [('1', 'One'), ('2', 'Two'), ('3', 'Three')]


class CrispyTestForm(forms.Form):

    FORM_CLASS = floppy_forms

    def __init__(self, *args, **kwargs):

        super(CrispyTestForm, self).__init__(*args, **kwargs)
        for field in base_fields:
            self.fields[field.lower()] = getattr(self.FORM_CLASS, field)(label=field.title(), required=False)


        
        field_list = list(self.fields.keys())
        self.helper = FormHelper()
        self.helper.form_id = 'fieldset-form'
        self.helper.layout = Layout(
            Fieldset(
                'This is a fieldset',
                *field_list
            ),
        )
