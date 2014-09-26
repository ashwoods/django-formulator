# -*- coding: utf-8 -*-
"""
Formulator Tests
"""

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.test import TestCase

import floppyforms as forms

from formulator.conf import settings
from formulator.models import Form, Field, FieldSet

from .forms import RegistrationForm

FIELDS = settings.FORMULATOR_FIELDS
REQUIRE_EXTRA_PARAMS = [
                        'RegexField',
                        'ComboField',
                        'TypedMultipleChoiceField',
                        'FilePathField',
]


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
        self.assertTrue(issubclass(form_class.form_class_factory(), forms.Form))

    def test_saved_form_factory(self):
        """
        Test that form_class_factory returns a subclass from Form
        """
        form_class = Form(name='test')
        form_class.save()
        self.assertTrue(issubclass(form_class.form_class_factory(), forms.Form))

    def test_form_instance(self):
        """
        Test that we can instantiate a dynamic form
        """
        form_class = Form(name='test').form_class_factory()
        form = form_class()
        self.assertIsInstance(form, form_class)


class CreateFormFields(TestCase):

    def setUp(self):
        """
        Set up: creates and saves models for form instance creation
        """
        form_class = Form(name='CustomForm')
        form_class.save()

        fieldset = FieldSet(form=form_class,
                            name='fieldset_1',
                            legend='This is a legend')
        fieldset.save()

        for field_type in FIELDS:
            field_class = field_type[1]
            field_name = field_type[0]
            if field_name in REQUIRE_EXTRA_PARAMS:
                pass
            else:
                Field.objects.create(
                                     formset=fieldset,
                                     name=field_name,
                                     field=field_name,
                                     label=field_name,
                                     help_text="test help text",
                                     attrs={"placeholder":field_name}
                )

        # Class variable for the form class
        self.form_class = form_class.form_class_factory()

        # A generator providing the fields in the form
        #import ipdb; ipdb.set_trace()
        self.field_getter = iter(self.form_class.base_fields.values())

    def test_form_with_default_fields(self):
        """
        Test that we have an instance form with fields
        """
        self.assertTrue(issubclass(self.form_class, forms.Form))

    def test_field_ordering(self):
        """
        Test that fields are ordered correctly according to position value
        """
        for f in FIELDS:
            if f[0] not in REQUIRE_EXTRA_PARAMS:
                self.assertTrue(f[0] in str(next(self.field_getter)))

    def test_required_field(self):
        """
        Test that fields required attribute is set to True by default
        """
        for field in self.field_getter:        
            self.assertTrue(field.required)

    def test_placeholder(self):
        """
        Test that the placeholder attribute is set
        """
        for field in self.field_getter:
            self.assertEquals(field.widget.attrs['placeholder'], field.label)

    def test_hidden(self):
        """
        Test that the hidden attribute is set to false by default
        """
        for field in self.field_getter:        
            self.assertFalse(field.show_hidden_initial)

    def test_help_text(self):
        """
        Test that the help text can be set
        """
        for field in self.field_getter:        
            self.assertEquals(field.help_text, "test help text")

    def test_label(self):
        """
        Test that the field label is set
        """
        for field in self.field_getter:        
            self.assertTrue(field.label in str(field.__class__))


class CreateRegistrationForm(TestCase):
    """A floppy forms test"""

    def test_clone_registration_form(self):
        # Composition of the form
        form_class = Form(name='RegistrationForm')
        form_class.save()

        # Composition of a Fieldset
        fieldset = FieldSet(form=form_class,
                            name='fieldset_1',
                            legend='This is a legend')
        fieldset.save()

        # Composition of the fields
        Field.objects.create(
            name="honeypot",
            field="CharField",
            required=False,
            widget="HiddenInput",
            formset=fieldset
        )
        Field.objects.create(
            name="firstname",
            field="CharField",
            label=_('Your first name?'),
            formset=fieldset
        )
        Field.objects.create(
            name="lastname",
            field="CharField",
            label=_('Your last name:'),
            formset=fieldset
        )
        Field.objects.create(
            name="username",
            field="CharField",
            attrs={"max_length": "30", "placeholder": "username here"},
            formset=fieldset
        )
        Field.objects.create(
            name="password",
            field="CharField",
            widget='PasswordInput',
            help_text=_('Make sure to use a secure password.'),
            formset=fieldset
        )
        Field.objects.create(
            name="password2",
            field="CharField",
            label=_('Retype password'),
            widget='PasswordInput',
            formset=fieldset
        )
        Field.objects.create(
            name="age",
            field="IntegerField",
            required=False,
            formset=fieldset
        )

        RegistrationFormClone = form_class.form_class_factory()
        
        # Assert that the HTML generated is the same
        self.assertEquals(RegistrationFormClone().as_p(), RegistrationForm().as_p(),)

    def test_compare_registration_form(self):
        pass
