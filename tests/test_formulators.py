# -*- coding: utf-8 -*-
"""
Formulator Tests
"""
import pytest
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


@pytest.mark.django_db
def formulator_form():
    """
    Creates and saves models for formulator instance creation
    """
    fm_form = Form.objects.create(name='test')
    fm_form.save()

    fm_fieldset = FieldSet.objects.create(
                                        form=fm_form,
                                        name='fieldset_1',
                                        legend='This is a legend')
    fm_fieldset.save()

    field = Field.objects.create(
                                fieldset=fm_fieldset,
                                name='Field',
                                field_type='Field')

    # A bunch of formulator fields, of all the FIELDS types
   # for field_type in FIELDS:
   #     field_name = field_type[0]
   #     field_class = field_type[1]
   #     if field_name in REQUIRE_EXTRA_PARAMS:
   #         pass
   #     else:
   #         Field(
   #                              name=field_name,
   #                              fieldset=fieldset,
   #                              label=field_name,
   #                              field=field_class,
   #                              help_text="test help text",
   #                              attrs={"placeholder":field_name}
   #         )
   # 
    # Class variable for the form class
    form_class = fm_form.form_class_factory()

    # A generator providing the fields in the form
    field_getter = iter(form_class.base_fields.values())

    return form_class

#@pytest.mark.django_db
#class TestCreateEmptyForm():
#    
#    def test_no_name_fails(self):
#        """
#        The Form needs a name, classes without names seem wrong.
#        """
#        # This should raise an AttributeError: 'Options' object has no attribute 'module_name'
#        with pytest.raises(AttributeError):
#            form_class = Form.objects.create()
#
#    def test_is_form_subclass(self):
#        """
#        Test that form_class_factory returns a subclass from DEFAULT_FORM_CLASS
#        """
#        formulator = Form.objects.create(name='test')
#        FORM_CLASS = formulator.form_class_factory()
#        assert issubclass(FORM_CLASS, settings.FORMULATOR_DEFAULT_FORM_CLASS)
#
#    def test_form_instance(self):
#        """
#        Test that we can instantiate a dynamic form
#        """
#        form_class = Form.objects.create(name='test').form_class_factory()
#        form = form_class()
#        assert isinstance(form, form_class)
#

@pytest.mark.django_db
class TestCreateFormFields():

    def test_form_with_default_fields(self):
        """
        Test that we have an instance form with fields
        """
        assert issubclass(formulator_form(), settings.FORMULATOR_DEFAULT_FORM_CLASS)

#    def test_field_ordering(self):
#        """
#        Test that fields are ordered correctly according to position value
#        """
#        for f in FIELDS:
#            if f[0] not in REQUIRE_EXTRA_PARAMS:
#                self.assertTrue(f[0] in str(next(self.field_getter)))
#
#    def test_required_field(self):
#        """
#        Test that fields required attribute is set to True by default
#        """
#        for field in self.field_getter:        
#            self.assertTrue(field.required)
#
#    def test_placeholder(self):
#        """
#        Test that the placeholder attribute is set
#        """
#        for field in self.field_getter:
#            self.assertEquals(field.widget.attrs['placeholder'], field.label)
#
#    def test_hidden(self):
#        """
#        Test that the hidden attribute is set to false by default
#        """
#        for field in self.field_getter:        
#            self.assertFalse(field.show_hidden_initial)
#
#    def test_help_text(self):
#        """
#        Test that the help text can be set
#        """
#        for field in self.field_getter:        
#            self.assertEquals(field.help_text, "test help text")
#
#    def test_label(self):
#        """
#        Test that the field label is set
#        """
#        for field in self.field_getter:        
#            self.assertTrue(field.label in str(field.__class__))
#
#
#class TestRepeatFields():
#
#    def setUp(self):
#        """
#        Set up: creates and saves models for form instance creation
#        """
#        form_class = Form(name='Form')
#        form_class.save()
#
#        fieldset = FieldSet(form=form_class,
#                            name='fieldset_1',
#                            legend='This is a legend')
#        fieldset.save()
#
#        # And a formulator field that will yield several form fields via the
#        # repeat_min attribute
#        self.field_name = 'foo'
#        self.rep_min = 2
#        self.rep_max = 5
#
#        Field.objects.create(formset=fieldset,
#                             name=self.field_name,
#                             field='CharField',
#                             repeat_min=self.rep_min,
#                             repeat_max=self.rep_max,
#        )
#
#        self.form_class = form_class.form_class_factory()
#
#    def test_repeat_min(self):
#        """
#        Test that number of fields yielded is the one expected
#        """
#        self.assertTrue(len(self.form_class.base_fields) == self.rep_min)
#
#    def test_repeat_max(self):
#        data_in_range = dict([(self.field_name + '_' + str(sub),'foo') for sub in range(0, self.rep_max)])
#        data_too_many = dict([(self.field_name + '_' + str(sub),'foo') for sub in range(0, self.rep_max + 3)])
#
#        # If the data is in range, the number of fields should be the same as in data
#        f = self.form_class(data_in_range)
#        self.assertEquals(len(f.fields), len(f.data))
#
#        # If the data is too many, the number of fields should be the same as maximum repetitions
#        f = self.form_class(data_too_many)
#        self.assertEquals(len(f.fields), self.rep_max)
#
#
#class TestCreateRegistrationForm():
#    """A floppy forms test"""
#
#    def test_clone_registration_form(self):
#        # Composition of the form
#        form_class = Form(name='RegistrationForm')
#        form_class.save()
#
#        # Composition of a Fieldset
#        fieldset = FieldSet(form=form_class,
#                            name='fieldset_1',
#                            legend='This is a legend')
#        fieldset.save()
#
#        # Composition of the fields
#        Field.objects.create(
#            name="honeypot",
#            field="CharField",
#            required=False,
#            widget="HiddenInput",
#            formset=fieldset
#        )
#        Field.objects.create(
#            name="firstname",
#            field="CharField",
#            label=_('Your first name?'),
#            formset=fieldset
#        )
#        Field.objects.create(
#            name="lastname",
#            field="CharField",
#            label=_('Your last name:'),
#            formset=fieldset
#        )
#        Field.objects.create(
#            name="username",
#            field="CharField",
#            attrs={"max_length": "30", "placeholder": "username here"},
#            formset=fieldset
#        )
#        Field.objects.create(
#            name="password",
#            field="CharField",
#            widget='PasswordInput',
#            help_text=_('Make sure to use a secure password.'),
#            formset=fieldset
#        )
#        Field.objects.create(
#            name="password2",
#            field="CharField",
#            label=_('Retype password'),
#            widget='PasswordInput',
#            formset=fieldset
#        )
#        Field.objects.create(
#            name="age",
#            field="IntegerField",
#            required=False,
#            formset=fieldset
#        )
#
#        RegistrationFormClone = form_class.form_class_factory()
#        
#        # Assert that the HTML generated is the same
#        self.assertEquals(RegistrationFormClone().as_p(), RegistrationForm().as_p(),)
#
#    def test_compare_registration_form(self):
#        pass
