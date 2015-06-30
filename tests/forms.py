# -*- coding: utf-8 -*-
"""
Formulator Tests
"""

from django.core.exceptions import ValidationError
from django import forms

import floppyforms as floppy_forms


base_fields = (
    'Field', 'CharField', 'IntegerField', 'DateField', 'TimeField',
    'DateTimeField', 'EmailField', 'FileField', 'ImageField', 'URLField',
    'BooleanField', 'NullBooleanField', 'ChoiceField', 'MultipleChoiceField',
    'FloatField', 'DecimalField', 'SlugField', 'IPAddressField',
    'GenericIPAddressField', 'TypedChoiceField',
    'TypedMultipleChoiceField', 'ComboField', 'MultiValueField',
    'SplitDateTimeField',
)

complex_fields = ('RegexField','FilePathField',)

class BaseForm(object):

    FORM_CLASS = None

    honeypot = forms.CharField(required=False, widget=forms.HiddenInput)
    firstname = forms.CharField(label='Your first name?')
    lastname = forms.CharField(label='Your last name:')
    username = forms.CharField(widget=forms.TextInput(attrs={'max_length': 30, 'placeholder': 'username here'}))
    password = forms.CharField(
        widget=forms.PasswordInput,
        help_text='Make sure to use a secure password.',
    )
    password2 = forms.CharField(label='Retype password', widget=forms.PasswordInput)
    age = forms.IntegerField(required=False)

    def __init__(self, *args , **kwargs):

        super(BaseForm, self).__init__(*args, **kwargs)
        for field in base_fields:
            print field
            self.fields['%s__field' % field.lower()] = getattr(self.FORM_CLASS, field)(label=field.title(), required=False)


    # extra fields

    # booleanfield
    # charfield ##
    #
    # choicefield ##
    # typedchoicefield ##
    # filepathfield ##
    #
    # datefield ##
    # datetimefield ##
    # decimalfield ##
    # emailfield ##
    # filefield ##
    # floatfield ##
    # imagefield ##
    # integerfield ##
    # multiplechoicefield ##
    # typedmultiplechoicefield ##
    #
    # nullbooleanfield ##
    # timefield ##
    # urlfield ##
    # slugfield ##
    # regexfield ##
    # ipaddressfield ##
    # genericipaddressfield ##

    # only django
    # uuidfield

    # complex field
    #combofield
    #mutlivaluefield
    #splitdatetimefield

    # relationship fields
    #modelmultiplechoicefield
    #modelchoicefield


    def clean_honeypot(self):
        if self.cleaned_data.get('honeypot'):
            raise ValidationError('Haha, you trapped into the honeypot.')
        return self.cleaned_data['honeypot']

    def clean(self):
        if self.errors:
            raise ValidationError('Please correct the errors below.')


class DjangoTestForm(BaseForm, forms.Form):
    FORM_CLASS = forms




class FloppyTestForm(BaseForm, floppy_forms.Form):
    pass

