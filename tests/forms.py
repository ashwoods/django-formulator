# -*- coding: utf-8 -*-
"""
Formulator Tests
"""

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

import floppyforms as forms


class RegistrationForm(forms.Form):

    honeypot = forms.CharField(required=False, widget=forms.HiddenInput)
    firstname = forms.CharField(label=_('Your first name?'))
    lastname = forms.CharField(label=_('Your last name:'))
    username = forms.CharField(widget=forms.TextInput(attrs={'max_length': 30, 'placeholder': 'username here'}))
    password = forms.CharField(
        widget=forms.PasswordInput,
        help_text=_('Make sure to use a secure password.'),
    )
    password2 = forms.CharField(label=_('Retype password'), widget=forms.PasswordInput)
    age = forms.IntegerField(required=False)

    def clean_honeypot(self):
        if self.cleaned_data.get('honeypot'):
            raise ValidationError('Haha, you trapped into the honeypot.')
        return self.cleaned_data['honeypot']

    def clean(self):
        if self.errors:
            raise ValidationError('Please correct the errors below.')
