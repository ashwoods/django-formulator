"""
Formulator Tests
"""
import importlib

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.test import TestCase
from formulator.models import Form, Field, FieldSet
from floppyforms.forms import BaseForm
from floppyforms import forms

from formulator.conf import settings


FIELDS = settings.FORMULATOR_FIELDS


# class RegistrationForm(forms.Form):
#     honeypot = forms.CharField(required=False, widget=forms.HiddenInput)
#     firstname = forms.CharField(label=_(u'Your first name?'))
#     lastname = forms.CharField(label=_(u'Your last name:'))
#     username = forms.CharField(max_length=30)
#     password = forms.CharField(
#         widget=forms.PasswordInput,
#         help_text=_(u'Make sure to use a secure password.'),
#     )
#     password2 = forms.CharField(label=_(u'Retype password'), widget=forms.PasswordInput)
#     age = forms.IntegerField(required=False)
#
#     def clean_honeypot(self):
#         if self.cleaned_data.get('honeypot'):
#             raise ValidationError(u'Haha, you trapped into the honeypot.')
#         return self.cleaned_data['honeypot']
#
#     def clean(self):
#         if self.errors:
#             raise ValidationError(u'Please correct the errors below.')


class CreateEmptyFormTest(TestCase):

    def test_no_name_factory(self):
        """
        The class factory needs a name, classes without names seem wrong
        """
        form_class = Form.objects.create()
        self.assertRaises(ValidationError, form_class.form_class_factory)

    def test_unsaved_form_factory(self):
        """
        Test that form_class_factory returns a subclass from Form
        We don't have to save the object (although makes little sense),
        """
        form_class = Form(name='test')
        self.assertTrue(issubclass(form_class.form_class_factory(), BaseForm))

    def test_saved_form_factory(self):
        """
        Test that form_class_factory returns a subclass from Form
        """
        form_class = Form(name='test')
        form_class.save()
        self.assertTrue(issubclass(form_class.form_class_factory(), BaseForm))

    def test_form_instance(self):
        """
        Test that we can instantiate a dynamic form
        """
        form_class = Form(name='test').form_class_factory()
        form = form_class()
        self.assertIsInstance(form, form_class)


class CreateFormFields(TestCase):

    def test_form_with_default_fields(self):
        """
        Test that we have an instance form with fields
        """
        form_class = Form(name='test')
        form_class.save()

        fieldset = FieldSet(form=form_class, name='fieldset_1', legend='This is a legend')
        fieldset.save()

        fields = {}

        REQUIRE_EXTRA_PARAMS = [
                                'RegexField',
                                'ComboField',
                                'TypedMultipleChoiceField',
                                'FilePathField',
        ]

        for field_type in FIELDS:
            field_class = field_type[1]
            field_name = field_type[0]
            if field_name in REQUIRE_EXTRA_PARAMS:
                pass
            else:
                fields[field_name.lower()] = Field.objects.create(name=field_name, formset=fieldset, field=field_name, label=field_name.lower())
        self.assertTrue(issubclass(form_class.form_class_factory(), BaseForm))


class CreateRegistrationForm(TestCase):
    """A floppy forms test"""
    pass
