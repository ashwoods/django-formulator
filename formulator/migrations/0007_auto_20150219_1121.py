# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formulator', '0006_auto_20150202_1340'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='field',
            options={'ordering': ['fieldset', 'position']},
        ),
        migrations.AlterModelOptions(
            name='fieldset',
            options={'ordering': ['form', 'position']},
        ),
        migrations.AlterField(
            model_name='field',
            name='field',
            field=models.CharField(max_length=100, choices=[(b'Field', b'floppyforms.fields.Field'), (b'CharField', b'floppyforms.fields.CharField'), (b'IntegerField', b'floppyforms.fields.IntegerField'), (b'DateField', b'floppyforms.fields.DateField'), (b'TimeField', b'floppyforms.fields.TimeField'), (b'DateTimeField', b'floppyforms.fields.DateTimeField'), (b'EmailField', b'floppyforms.fields.EmailField'), (b'FileField', b'floppyforms.fields.FileField'), (b'ImageField', b'floppyforms.fields.ImageField'), (b'URLField', b'floppyforms.fields.URLField'), (b'BooleanField', b'floppyforms.fields.BooleanField'), (b'NullBooleanField', b'floppyforms.fields.NullBooleanField'), (b'ChoiceField', b'floppyforms.fields.ChoiceField'), (b'MultipleChoiceField', b'floppyforms.fields.MultipleChoiceField'), (b'FloatField', b'floppyforms.fields.FloatField'), (b'DecimalField', b'floppyforms.fields.DecimalField'), (b'SlugField', b'floppyforms.fields.SlugField'), (b'RegexField', b'floppyforms.fields.RegexField'), (b'IPAddressField', b'floppyforms.fields.IPAddressField'), (b'GenericIPAddressField', b'floppyforms.fields.GenericIPAddressField'), (b'TypedChoiceField', b'floppyforms.fields.TypedChoiceField'), (b'FilePathField', b'floppyforms.fields.FilePathField'), (b'TypedMultipleChoiceField', b'floppyforms.fields.TypedMultipleChoiceField'), (b'ComboField', b'floppyforms.fields.ComboField'), (b'MultiValueField', b'floppyforms.fields.MultiValueField'), (b'SplitDateTimeField', b'floppyforms.fields.SplitDateTimeField'), (b'CountryChoiceField', b'submitz.utils.helpers.CountryChoiceField'), (b'CountTextAreaField', b'floppy_charcount.fields.CountTextAreaField')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='field',
            name='widget',
            field=models.CharField(blank=True, help_text="A Widget class, or instance of a Widget class, that should\n                                           be used for this Field when displaying it. Each Field has a\n                                           default Widget that it'll use if you don't specify this. In\n                                           most cases, the default widget is TextInput.", max_length=100, choices=[(b'TextInput', b'floppyforms.widgets.TextInput'), (b'PasswordInput', b'floppyforms.widgets.PasswordInput'), (b'HiddenInput', b'floppyforms.widgets.HiddenInput'), (b'ClearableFileInput', b'floppyforms.widgets.ClearableFileInput'), (b'FileInput', b'floppyforms.widgets.FileInput'), (b'DateInput', b'floppyforms.widgets.DateInput'), (b'DateTimeInput', b'floppyforms.widgets.DateTimeInput'), (b'TimeInput', b'floppyforms.widgets.TimeInput'), (b'Textarea', b'floppyforms.widgets.Textarea'), (b'CheckboxInput', b'floppyforms.widgets.CheckboxInput'), (b'Select', b'floppyforms.widgets.Select'), (b'NullBooleanSelect', b'floppyforms.widgets.NullBooleanSelect'), (b'SelectMultiple', b'floppyforms.widgets.SelectMultiple'), (b'RadioSelect', b'floppyforms.widgets.RadioSelect'), (b'CheckboxSelectMultiple', b'floppyforms.widgets.CheckboxSelectMultiple'), (b'SearchInput', b'floppyforms.widgets.SearchInput'), (b'RangeInput', b'floppyforms.widgets.RangeInput'), (b'ColorInput', b'floppyforms.widgets.ColorInput'), (b'EmailInput', b'floppyforms.widgets.EmailInput'), (b'URLInput', b'floppyforms.widgets.URLInput'), (b'PhoneNumberInput', b'floppyforms.widgets.PhoneNumberInput'), (b'NumberInput', b'floppyforms.widgets.NumberInput'), (b'IPAddressInput', b'floppyforms.widgets.IPAddressInput'), (b'MultiWidget', b'floppyforms.widgets.MultiWidget'), (b'Widget', b'floppyforms.widgets.Widget'), (b'SplitDateTimeWidget', b'floppyforms.widgets.SplitDateTimeWidget'), (b'SplitHiddenDateTimeWidget', b'floppyforms.widgets.SplitHiddenDateTimeWidget'), (b'MultipleHiddenInput', b'floppyforms.widgets.MultipleHiddenInput'), (b'SelectDateWidget', b'floppyforms.widgets.SelectDateWidget'), (b'SlugInput', b'floppyforms.widgets.SlugInput'), (b'CountrySelectWidget', b'django_countries.widgets.CountrySelectWidget')]),
            preserve_default=True,
        ),
    ]
