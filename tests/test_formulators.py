# -*- coding: utf-8 -*-
"""
Formulator Tests
"""
import pytest
from formulator.conf import settings
from formulator.models import Form, Field, FieldSet, FieldAttribute, WidgetAttribute

from .forms import FloppyTestForm

FIELDS = settings.FORMULATOR_FIELDS
REQUIRE_EXTRA_PARAMS = [
                        'RegexField',
                        'ComboField',
                        'TypedMultipleChoiceField',
                        'FilePathField',
]





@pytest.mark.django_db
def get_formulator_form():
    """
    Creates and saves models for formulator instance creation
    """
    fm_form = Form.objects.create(name='test')
    Field.objects.create(
                        form=fm_form,
                        name='Field',
                        field_type='Field')

    Field.objects.create(
           name="honeypot",
           field_type="CharField",
           required=False,
           widget="HiddenInput",
           form=fm_form
       )

    Field.objects.create(
           name="firstname",
           field_type="CharField",
           label='Your first name?',
           form=fm_form
       )

    Field.objects.create(
           name="lastname",
           field_type="CharField",
           label='Your last name:',
           form=fm_form
       )

    field1 = Field.objects.create(
           name="username",
           field_type="CharField",
           form=fm_form,
           max_length=30,
           placeholder='username here',

       )


    #field1.widgetattribute_set.create(key='max_length', value=30)
    #field1.widgetattribute_set.create(key='placeholder', value='username here')


    Field.objects.create(
           name="password",
           field_type="CharField",
           widget='PasswordInput',
           help_text='Make sure to use a secure password.',
           form=fm_form
    )
    Field.objects.create(
           name="password2",
           field_type="CharField",
           label='Retype password',
           widget='PasswordInput',
           form=fm_form
    )
    Field.objects.create(
           name="age",
           field_type="IntegerField",
           required=False,
           form=fm_form
    )



    return fm_form


@pytest.mark.django_db
class TestDjangoFormFormulators():

    def test_form_class(self):
        """
        Test that we have an instance form with fields
        """
        assert issubclass(get_formulator_form().form_class_factory(), settings.FORMULATOR_DEFAULT_FORM_CLASS)


    def test_field_classes(self):
        """
        Test form html equality
        """
        django_form = FloppyTestForm()
        formulator_form = get_formulator_form().form_class_factory()()
        for item in zip(django_form, formulator_form):
            assert(type(item[0]) is type(item[1]))

    def test_fields_length(self):

        django_form = FloppyTestForm()
        formulator_form = get_formulator_form().form_class_factory()()
        assert len(django_form.fields) == len(formulator_form.fields)

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
