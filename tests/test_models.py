# -*- coding: utf-8 -*-
"""
Formulator Tests
"""
import pytest


@pytest.mark.django_db
def test_form_class(form_factory, default_form_class):
    """
    Test that we have an instance form with fields
    """
    formulator_form_class = form_factory().form_factory()
    assert issubclass(formulator_form_class, default_form_class)
#
#
# @pytest.mark.django_db
# def test_field_classes(django_honeypot_form, formulator_honeypot_form):
#     """
#     Tests that both form fields have the same classes (and in the same order +=)
#     """
#     formulator_form_instance = formulator_honeypot_form.form_factory()()
#     django_form_instance = django_honeypot_form()
#     for item in zip(django_form_instance, formulator_form_instance):
#         assert(isinstance(item[0], type(item[1])))
#     #
    # def test_fields_length(self):
    #
    #     django_form = FloppyTestForm()
    #     formulator_form = get_formulator_form().form_class_factory()()
    #     assert len(django_form.fields) == len(formulator_form.fields)
    #
    # def test_html_output(self):
    #     """
    #     Test form html equality
    #     """
    #     django_form = FloppyTestForm()
    #     formulator_form = get_formulator_form().form_class_factory()()
    #     assert(render_form(django_form, use_crispy=False) == render_form(formulator_form, use_crispy=False))
    #
    # def test_choices(self):
    #     """
    #     Tests that choices have been set for ChoiceField
    #     """
    #     django_form = FloppyTestForm()
    #     formulator_form = get_formulator_form().form_class_factory()()
    #     choices = formulator_form.fields['choicefield'].choices
    #     assert choices == [('1', 'One'), ('2', 'Two'), ('3', 'Three')]



    #
    # def test_fieldset(self):
    #     """
    #     Test that the form has a fieldset
    #     """
    #     formulator_form = get_formulator_fieldset_form().form_class_factory()()
    #     fs = formulator_form.helper.layout.fields[0]
    #     assert(isinstance(fs, Fieldset))
    #
    # def test_html_output(self):
    #     """
    #     Test form html equality
    #     """
    #     django_form = CrispyTestForm()
    #     formulator_form = get_formulator_fieldset_form().form_class_factory()()
    #     assert(render_form(django_form, use_crispy=True) == render_form(formulator_form, use_crispy=True))
