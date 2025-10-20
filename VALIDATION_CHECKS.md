# Field and Widget Validation Checks

This document describes the validation checks added to ensure that all `field_type` and `widget` values in Field instances are valid importable Python classes.

## Overview

The validation checks run as part of Django's system checks framework and will automatically verify that:
1. All `field_type` values are valid Python import paths to form field classes
2. All `widget` values are valid Python import paths to widget classes

## How It Works

The checks are implemented in `formulator/checks.py` and are automatically registered with Django when the app is loaded. They run:
- When you execute `python manage.py check`
- Before running migrations
- When starting the development server

## Check IDs

- **formulator.E001**: Invalid field_type detected
- **formulator.E002**: Invalid widget detected

## Example Errors

### Invalid Field Type
```
SystemCheckError: System check identified some issues:

ERRORS:
formulator.Field: (formulator.E001) Invalid field_type 'nonexistent.module.CharField' for Field #2 (Test Field)
    HINT: Ensure the field_type is a valid Python import path to a form field class.
```

### Invalid Widget
```
SystemCheckError: System check identified some issues:

ERRORS:
formulator.Field: (formulator.E002) Invalid widget 'invalid.widget.TextInput' for Field #3 (Test Field)
    HINT: Ensure the widget is a valid Python import path to a widget class.
```

## Usage

### Running Checks Manually

```bash
python manage.py check
```

### In Tests

You can test the validation checks directly:

```python
from formulator.checks import check_field_types, check_widget_types

# Run checks
field_errors = check_field_types(app_configs=None)
widget_errors = check_widget_types(app_configs=None)

# Check for errors
if field_errors or widget_errors:
    print("Validation errors found!")
```

### Preventing Invalid Data

The checks help catch configuration errors early. For example:

```python
from formulator.models import Form, Field

# This will be flagged by the check system
form = Form.objects.create(name='My Form')
Field.objects.create(
    form=form,
    label='Bad Field',
    field_type='does.not.exist.CharField',  # Invalid!
    position=0
)

# Run Django's check command to catch the error
# python manage.py check
```

## Implementation Details

### Check Functions

The checks are implemented as two separate functions:

1. **check_field_types()**: Validates all `field_type` values
2. **check_widget_types()**: Validates all `widget` values

Both functions:
- Query all Field instances from the database
- Attempt to import each class string
- Report errors for any that fail to import
- Gracefully handle cases where the database tables don't exist yet (e.g., before migrations)

### Registration

The checks are registered in `formulator/apps.py`:

```python
class DynamicFormsConfig(AppConfig):
    name = 'formulator'
    verbose_name = _("Formulator")
    
    def ready(self):
        # Import checks to register them with Django's check framework
        from formulator import checks  # noqa
```

## Testing

The validation checks include comprehensive test coverage in `tests/test_checks.py`:

- Valid field_type and widget values produce no errors
- Invalid module names are detected
- Invalid class names are detected
- Malformed import paths are detected
- Multiple invalid values produce multiple errors
- Empty/blank widget values are handled correctly

Run the tests:
```bash
pytest tests/test_checks.py -v
```
