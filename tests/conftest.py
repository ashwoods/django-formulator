# -*- coding: utf-8 -*-
import pytest
from pytest_factoryboy import register

from django.conf import settings

from formulator.factories import FormFactory, FieldFactory, ChoiceFactory
from formulator.utils import import_class


from .forms import TestForm

register(FormFactory)
register(FieldFactory)
register(ChoiceFactory)


@pytest.fixture
def django_honeypot_form():
    return TestForm


@pytest.fixture
def default_form_class():
    return import_class(settings.FORMULATOR_FORM_CLASS)


from django.template import Context, Template


# def render_form(form, use_crispy=False):
#     if use_crispy:
#         template = "{% load crispy_forms_tags %} {% crispy form %}"
#     else:
#         template = "{{form}}"
#     return Template(template).render(Context({'form': form}))
#
# @pytest.fixture
# def formulator_honeypot_form(form, field_factory):
#     """
#     Honeypot form example
#     """
#     field_factory(
#         name="honeypot",
#         field_type="floppyforms.fields.CharField",
#         required=False,
#         widget="django.forms.widgets.HiddenInput",
#         form=form,
#         position=0
#     )
#
#     field_factory(
#         name="firstname",
#         field_type="floppyforms.fields.CharField",
#         label='Your first name?',
#         form=form,
#         required=True,
#         position=1
#     )
#
#     field_factory(
#         name="lastname",
#         field_type="floppyforms.fields.CharField",
#         label='Your last name:',
#         form=form,
#         required=True,
#         position=2
#     )
#
#     field_factory(
#         name="username",
#         label="Username:",
#         field_type="floppyforms.fields.CharField",
#         form=form,
#         max_length=30,
#         placeholder='username here',
#         position=3
#     )
#
#     field_factory(
#         name="password",
#         label='Password:',
#         field_type="floppyforms.fields.CharField",
#         widget='floppyforms.widgets.PasswordInput',
#         help_text='Make sure to use a secure password.',
#         form=form,
#         required=True,
#         position=4
#     )
#
#     field_factory(
#         name="password2",
#         field_type="floppyforms.fields.CharField",
#         label='Retype password',
#         widget='floppyforms.widgets.PasswordInput',
#         form=form,
#         required=True,
#         position=5
#     )
#
#     field_factory(
#         name="age",
#         label="Age:",
#         field_type="floppyforms.fields.IntegerField",
#         required=False,
#         form=form,
#         position=6
#     )
#
#     choice_field = form.field_set.get(field_id='choicefield')
#
#     choice_factory(field=choice_field, key=1, value="One")
#     choice_factory(field=choice_field, key=2, value="Two")
#     choice_factory(field=choice_field, key=3, value="Three")
#
#     return form
