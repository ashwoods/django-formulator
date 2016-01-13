# -*- coding: utf-8 -*-
"""
Formulator Tests
"""
import pytest

from django.template import Context, Template

from formulator.conf import settings
from formulator.models import Form, Field, FieldSet, Choice
from crispy_forms.layout import Fieldset

from .forms import FloppyTestForm, CrispyTestForm, base_fields

REQUIRE_EXTRA_PARAMS = [
    'RegexField',
    'ComboField',
    'TypedMultipleChoiceField',
    'FilePathField',
]


def render_form(form, use_crispy=False):
    if use_crispy:
        template = "{% load crispy_forms_tags %} {% crispy form %}"
    else:
        template = "{{form}}"
    return Template(template).render(Context({'form': form}))


@pytest.mark.django_db
def get_formulator_form():
    """
    Creates and saves models for formulator instance creation
    """
    fm_form = Form.objects.create(name='Honeypot form')

    Field.objects.create(
        name="honeypot",
        field_type="floppyforms.fields.CharField",
        required=False,
        widget="django.forms.widgets.HiddenInput",
        form=fm_form,
        position=0
    )

    Field.objects.create(
        name="firstname",
        field_type="floppyforms.fields.CharField",
        label='Your first name?',
        form=fm_form,
        required=True,
        position=1
    )

    Field.objects.create(
        name="lastname",
        field_type="floppyforms.fields.CharField",
        label='Your last name:',
        form=fm_form,
        required=True,
        position=2
    )

    Field.objects.create(
        name="username",
        label="Username:",
        field_type="floppyforms.fields.CharField",
        form=fm_form,
        max_length=30,
        placeholder='username here',
        position=3
    )

    Field.objects.create(
        name="password",
        label='Password:',
        field_type="floppyforms.fields.CharField",
        widget='floppyforms.widgets.PasswordInput',
        help_text='Make sure to use a secure password.',
        form=fm_form,
        required=True,
        position=4
    )

    Field.objects.create(
        name="password2",
        field_type="floppyforms.fields.CharField",
        label='Retype password',
        widget='floppyforms.widgets.PasswordInput',
        form=fm_form,
        required=True,
        position=5
    )

    Field.objects.create(
        name="age",
        label="Age:",
        field_type="floppyforms.fields.IntegerField",
        required=False,
        form=fm_form,
        position=6
    )

    pos = 7
    
    for field_type in base_fields:
        Field.objects.create(
            name=field_type.title(),
            label="%s:" % field_type.title(),
            field_type='floppyforms.fields.' + field_type,
            required=False,
            form=fm_form,
            position=pos
        )
        
        pos += 1

    # Set choices for choicefield
    choice_field = fm_form.field_set.get(field_id='choicefield')
    
    Choice.objects.create(field=choice_field, key=1, value="One")
    Choice.objects.create(field=choice_field, key=2, value="Two")
    Choice.objects.create(field=choice_field, key=3, value="Three")

    return fm_form


@pytest.mark.django_db
def get_formulator_fieldset_form():
    """
    Creates and saves models for formulator instance creation
    """
    fm_form = Form.objects.create(name='Fieldset form')

    fm_fieldset = FieldSet.objects.create(
        name="Fieldset",
        legend="This is a fieldset",
        form=fm_form
    )

    pos = 0

    for field_type in base_fields:
        Field.objects.create(
            name=field_type.title(),
            label=field_type.title(),
            field_type='floppyforms.fields.' + field_type,
            required=False,
            form=fm_form,
            fieldset=fm_fieldset,
            position=pos
        )

        pos += 1

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
        Tests that both form fields have the same classes (and in the same order +=)
        """
        django_form = FloppyTestForm()
        formulator_form = get_formulator_form().form_class_factory()()
        for item in zip(django_form, formulator_form):
            assert(isinstance(item[0], type(item[1])))

    def test_fields_length(self):

        django_form = FloppyTestForm()
        formulator_form = get_formulator_form().form_class_factory()()
        assert len(django_form.fields) == len(formulator_form.fields)

    def test_html_output(self):
        """
        Test form html equality
        """
        django_form = FloppyTestForm()
        formulator_form = get_formulator_form().form_class_factory()()
        assert(render_form(django_form, use_crispy=False) == render_form(formulator_form, use_crispy=False))

    def test_choices(self):
        """
        Tests that choices have been set for ChoiceField
        """
        django_form = FloppyTestForm()
        formulator_form = get_formulator_form().form_class_factory()()
        choices = formulator_form.fields['choicefield'].choices 
        assert choices == [('1', 'One'), ('2', 'Two'), ('3', 'Three')]


@pytest.mark.django_db
class TestDjangoFormFieldsetFormulators():

    def test_fieldset(self):
        """
        Test that the form has a fieldset
        """
        formulator_form = get_formulator_fieldset_form().form_class_factory()()
        fs = formulator_form.helper.layout.fields[0]
        assert(isinstance(fs, Fieldset))

    def test_html_output(self):
        """
        Test form html equality
        """
        django_form = CrispyTestForm()
        formulator_form = get_formulator_fieldset_form().form_class_factory()()
        assert(render_form(django_form, use_crispy=True) == render_form(formulator_form, use_crispy=True))
