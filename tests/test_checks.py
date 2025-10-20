# -*- coding: utf-8 -*-
"""
Tests for Django system checks on formulator models
"""
import pytest
from django.core.checks import Error

from formulator.models import Form, Field
from formulator.checks import check_field_types, check_widget_types


@pytest.mark.django_db
class TestFieldValidationChecks:
    """Test that field_type validation checks work correctly"""
    
    def test_valid_field_type(self):
        """Valid field types should not produce errors"""
        form = Form.objects.create(name='Test Form')
        Field.objects.create(
            form=form,
            label='Test Field',
            field_type='floppyforms.fields.CharField',
            position=0
        )
        
        errors = check_field_types(app_configs=None)
        assert len(errors) == 0
    
    def test_invalid_field_type_module(self):
        """Invalid module in field_type should produce an error"""
        form = Form.objects.create(name='Test Form')
        field = Field.objects.create(
            form=form,
            label='Test Field',
            field_type='nonexistent.module.CharField',
            position=0
        )
        
        errors = check_field_types(app_configs=None)
        assert len(errors) == 1
        assert isinstance(errors[0], Error)
        assert errors[0].id == 'formulator.E001'
        assert 'nonexistent.module.CharField' in errors[0].msg
        assert str(field.pk) in errors[0].msg
    
    def test_invalid_field_type_class(self):
        """Invalid class name in field_type should produce an error"""
        form = Form.objects.create(name='Test Form')
        field = Field.objects.create(
            form=form,
            label='Test Field',
            field_type='floppyforms.fields.NonExistentField',
            position=0
        )
        
        errors = check_field_types(app_configs=None)
        assert len(errors) == 1
        assert isinstance(errors[0], Error)
        assert errors[0].id == 'formulator.E001'
        assert 'floppyforms.fields.NonExistentField' in errors[0].msg
    
    def test_invalid_field_type_format(self):
        """Malformed field_type should produce an error"""
        form = Form.objects.create(name='Test Form')
        field = Field.objects.create(
            form=form,
            label='Test Field',
            field_type='InvalidFormat',
            position=0
        )
        
        errors = check_field_types(app_configs=None)
        assert len(errors) == 1
        assert isinstance(errors[0], Error)
        assert errors[0].id == 'formulator.E001'
    
    def test_multiple_invalid_field_types(self):
        """Multiple invalid field types should produce multiple errors"""
        form = Form.objects.create(name='Test Form')
        Field.objects.create(
            form=form,
            label='Test Field 1',
            field_type='invalid.field.Type1',
            position=0
        )
        Field.objects.create(
            form=form,
            label='Test Field 2',
            field_type='invalid.field.Type2',
            position=1
        )
        
        errors = check_field_types(app_configs=None)
        assert len(errors) == 2
        assert all(isinstance(error, Error) for error in errors)
        assert all(error.id == 'formulator.E001' for error in errors)


@pytest.mark.django_db
class TestWidgetValidationChecks:
    """Test that widget validation checks work correctly"""
    
    def test_valid_widget(self):
        """Valid widgets should not produce errors"""
        form = Form.objects.create(name='Test Form')
        Field.objects.create(
            form=form,
            label='Test Field',
            field_type='floppyforms.fields.CharField',
            widget='django.forms.widgets.TextInput',
            position=0
        )
        
        errors = check_widget_types(app_configs=None)
        assert len(errors) == 0
    
    def test_empty_widget(self):
        """Empty widget should not produce an error"""
        form = Form.objects.create(name='Test Form')
        Field.objects.create(
            form=form,
            label='Test Field',
            field_type='floppyforms.fields.CharField',
            widget='',
            position=0
        )
        
        errors = check_widget_types(app_configs=None)
        assert len(errors) == 0
    
    def test_invalid_widget_module(self):
        """Invalid module in widget should produce an error"""
        form = Form.objects.create(name='Test Form')
        field = Field.objects.create(
            form=form,
            label='Test Field',
            field_type='floppyforms.fields.CharField',
            widget='nonexistent.module.TextInput',
            position=0
        )
        
        errors = check_widget_types(app_configs=None)
        assert len(errors) == 1
        assert isinstance(errors[0], Error)
        assert errors[0].id == 'formulator.E002'
        assert 'nonexistent.module.TextInput' in errors[0].msg
        assert str(field.pk) in errors[0].msg
    
    def test_invalid_widget_class(self):
        """Invalid class name in widget should produce an error"""
        form = Form.objects.create(name='Test Form')
        field = Field.objects.create(
            form=form,
            label='Test Field',
            field_type='floppyforms.fields.CharField',
            widget='django.forms.widgets.NonExistentWidget',
            position=0
        )
        
        errors = check_widget_types(app_configs=None)
        assert len(errors) == 1
        assert isinstance(errors[0], Error)
        assert errors[0].id == 'formulator.E002'
        assert 'django.forms.widgets.NonExistentWidget' in errors[0].msg
    
    def test_multiple_invalid_widgets(self):
        """Multiple invalid widgets should produce multiple errors"""
        form = Form.objects.create(name='Test Form')
        Field.objects.create(
            form=form,
            label='Test Field 1',
            field_type='floppyforms.fields.CharField',
            widget='invalid.widget.Type1',
            position=0
        )
        Field.objects.create(
            form=form,
            label='Test Field 2',
            field_type='floppyforms.fields.CharField',
            widget='invalid.widget.Type2',
            position=1
        )
        
        errors = check_widget_types(app_configs=None)
        assert len(errors) == 2
        assert all(isinstance(error, Error) for error in errors)
        assert all(error.id == 'formulator.E002' for error in errors)


@pytest.mark.django_db
class TestCombinedValidationChecks:
    """Test that both field and widget checks work together"""
    
    def test_both_field_and_widget_invalid(self):
        """Invalid field_type and widget should produce two errors"""
        form = Form.objects.create(name='Test Form')
        Field.objects.create(
            form=form,
            label='Test Field',
            field_type='invalid.field.Type',
            widget='invalid.widget.Type',
            position=0
        )
        
        field_errors = check_field_types(app_configs=None)
        widget_errors = check_widget_types(app_configs=None)
        
        assert len(field_errors) == 1
        assert len(widget_errors) == 1
        assert field_errors[0].id == 'formulator.E001'
        assert widget_errors[0].id == 'formulator.E002'
    
    def test_valid_field_invalid_widget(self):
        """Valid field_type but invalid widget should only produce widget error"""
        form = Form.objects.create(name='Test Form')
        Field.objects.create(
            form=form,
            label='Test Field',
            field_type='floppyforms.fields.CharField',
            widget='invalid.widget.Type',
            position=0
        )
        
        field_errors = check_field_types(app_configs=None)
        widget_errors = check_widget_types(app_configs=None)
        
        assert len(field_errors) == 0
        assert len(widget_errors) == 1
