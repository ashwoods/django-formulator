# -*- coding: utf-8 -*-
"""
Formulator Test Forms
"""

from django.core.exceptions import ValidationError
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset


class TestForm(forms.Form):

    honeypot = forms.CharField(required=False, widget=forms.HiddenInput)
    firstname = forms.CharField(label='Your first name?', required=True)
    lastname = forms.CharField(label='Your last name:')
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'max_length': 30, 'placeholder': 'username here'}
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput,
        help_text='Make sure to use a secure password.',
    )
    password2 = forms.CharField(label='Retype password', widget=forms.PasswordInput)
    age = forms.IntegerField(required=False)

    def __init__(self, *args, **kwargs):

        super(TestForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_id = 'fieldset-form'
        self.helper.layout = Layout(
            Fieldset(
                'This is a fieldset',
                *self.fields.keys()
            ),
        )

    def clean_honeypot(self):
        if self.cleaned_data.get('honeypot'):
            raise ValidationError('Haha, you trapped into the honeypot.')
        return self.cleaned_data['honeypot']

    def clean(self):
        if self.errors:
            raise ValidationError('Please correct the errors below.')

