# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import importlib

from django.core.checks import Error, register, Tags


def import_class(class_path):
    """
    Attempts to import a class from a string path.
    Returns the class if successful, None otherwise.
    """
    try:
        module_name, class_name = class_path.rsplit(".", 1)
        module = importlib.import_module(module_name)
        return getattr(module, class_name)
    except (ValueError, ImportError, AttributeError):
        return None


@register(Tags.models)
def check_field_types(app_configs, **kwargs):
    """
    Check that all field_type values in Field instances are valid importable classes.
    """
    from formulator.models import Field
    from django.db import connection
    from django.db.utils import OperationalError, ProgrammingError
    
    errors = []
    
    # Check if the table exists before querying
    table_name = Field._meta.db_table
    if table_name not in connection.introspection.table_names():
        # Table doesn't exist yet, skip check (migrations haven't run)
        return errors
    
    # Only check if the Field model exists and has data
    try:
        fields = Field.objects.all()
    except (OperationalError, ProgrammingError):
        # If we can't query the database (e.g., migrations haven't run), skip the check
        return errors
    
    for field in fields:
        if field.field_type:
            field_class = import_class(field.field_type)
            if field_class is None:
                errors.append(
                    Error(
                        "Invalid field_type '%s' for Field #%d (%s)" % (
                            field.field_type, field.pk, field.label
                        ),
                        hint="Ensure the field_type is a valid Python import path to a form field class.",
                        obj=field,
                        id='formulator.E001',
                    )
                )
    
    return errors


@register(Tags.models)
def check_widget_types(app_configs, **kwargs):
    """
    Check that all widget values in Field instances are valid importable classes.
    """
    from formulator.models import Field
    from django.db import connection
    from django.db.utils import OperationalError, ProgrammingError
    
    errors = []
    
    # Check if the table exists before querying
    table_name = Field._meta.db_table
    if table_name not in connection.introspection.table_names():
        # Table doesn't exist yet, skip check (migrations haven't run)
        return errors
    
    # Only check if the Field model exists and has data
    try:
        fields = Field.objects.all()
    except (OperationalError, ProgrammingError):
        # If we can't query the database (e.g., migrations haven't run), skip the check
        return errors
    
    for field in fields:
        if field.widget:
            widget_class = import_class(field.widget)
            if widget_class is None:
                errors.append(
                    Error(
                        "Invalid widget '%s' for Field #%d (%s)" % (
                            field.widget, field.pk, field.label
                        ),
                        hint="Ensure the widget is a valid Python import path to a widget class.",
                        obj=field,
                        id='formulator.E002',
                    )
                )
    
    return errors
