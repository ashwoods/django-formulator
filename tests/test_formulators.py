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
def test_is_form_subclass():
    """
    Test that form_class_factory returns a subclass from Form
    """
    formulator = Form.objects.create(name='test')
    FORM_CLASS = formulator.form_class_factory()
    assert issubclass(FORM_CLASS, settings.FORMULATOR_DEFAULT_FORM_CLASS)



