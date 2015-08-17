# -*- coding: utf-8 -*-
"""
Formulator Tests
"""
import pytest

from django.template import Context, Template

from formulator.conf import settings
from formulator.models import Form, Field, FieldSet, FieldAttribute, WidgetAttribute
from .forms import FloppyTestForm, CrispyTestForm, base_fields

FIELDS = settings.FORMULATOR_FIELDS
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
           field_type="CharField",
           required=False,
           widget="HiddenInput",
           form=fm_form,
       )

    Field.objects.create(
           name="firstname",
           field_type="CharField",
           label='Your first name?',
           form=fm_form,
           required=True
       )

    Field.objects.create(
           name="lastname",
           field_type="CharField",
           label='Your last name:',
           form=fm_form,
           required=True,
       )

    Field.objects.create(
           name="username",
           label="Username:",
           field_type="CharField",
           form=fm_form,
           max_length=30,
           placeholder='username here',

       )

    Field.objects.create(
           name="password",
           label='Password:',
           field_type="CharField",
           widget='PasswordInput',
           help_text='Make sure to use a secure password.',
           form=fm_form,
           required=True,
    )

    Field.objects.create(
           name="password2",
           field_type="CharField",
           label='Retype password',
           widget='PasswordInput',
           form=fm_form,
           required=True,
    )

    Field.objects.create(
           name="age",
           label="Age:",
           field_type="IntegerField",
           required=False,
           form=fm_form
    )

    for field_type in base_fields:
        Field.objects.create(name=field_type.title(), label="%s:" % field_type.title(), field_type=field_type, required=False, form=fm_form)

    return fm_form

@pytest.mark.django_db
def get_formulator_fieldset_form():
    """
    Creates and saves models for formulator instance creation
    """
    fm_form = Form.objects.create(name='Fielset form')

    fm_fieldset = FieldSet.objects.create(
                            name="Fieldset",
                            legend="This is a fieldset",
                            form=fm_form            
                        )

    for field_type in base_fields:
        Field.objects.create(
                name=field_type.title(),
                label="%s:" % field_type.title(),
                field_type=field_type,
                required=False,
                form=fm_form,
                fieldset=fm_fieldset
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
        Tests that both form fields have the same classes (and in the same order +=)
        """
        django_form = FloppyTestForm()
        formulator_form = get_formulator_form().form_class_factory()()
        for item in zip(django_form, formulator_form):
            assert(type(item[0]) is type(item[1]))

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



@pytest.mark.django_db
class TestDjangoFormFieldsetFormulators():

    def test_html_output(self):
        """
        Test form html equality
        """
        django_form = CrispyTestForm()
        formulator_form = get_formulator_fieldset_form().form_class_factory()()
        import ipdb; ipdb.set_trace()
        assert(render_form(django_form, use_crispy=True) == render_form(formulator_form, use_crispy=True))

