# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formulator', '0003_auto_20150112_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='field',
            name='field',
            field=models.CharField(max_length=100, choices=[(b'Field', b'floppyforms.fields.Field'), (b'CharField', b'floppyforms.fields.CharField'), (b'IntegerField', b'floppyforms.fields.IntegerField'), (b'DateField', b'floppyforms.fields.DateField'), (b'TimeField', b'floppyforms.fields.TimeField'), (b'DateTimeField', b'floppyforms.fields.DateTimeField'), (b'EmailField', b'floppyforms.fields.EmailField'), (b'FileField', b'floppyforms.fields.FileField'), (b'ImageField', b'floppyforms.fields.ImageField'), (b'URLField', b'floppyforms.fields.URLField'), (b'BooleanField', b'floppyforms.fields.BooleanField'), (b'NullBooleanField', b'floppyforms.fields.NullBooleanField'), (b'ChoiceField', b'floppyforms.fields.ChoiceField'), (b'MultipleChoiceField', b'floppyforms.fields.MultipleChoiceField'), (b'FloatField', b'floppyforms.fields.FloatField'), (b'DecimalField', b'floppyforms.fields.DecimalField'), (b'SlugField', b'floppyforms.fields.SlugField'), (b'RegexField', b'floppyforms.fields.RegexField'), (b'IPAddressField', b'floppyforms.fields.IPAddressField'), (b'GenericIPAddressField', b'floppyforms.fields.GenericIPAddressField'), (b'TypedChoiceField', b'floppyforms.fields.TypedChoiceField'), (b'FilePathField', b'floppyforms.fields.FilePathField'), (b'TypedMultipleChoiceField', b'floppyforms.fields.TypedMultipleChoiceField'), (b'ComboField', b'floppyforms.fields.ComboField'), (b'MultiValueField', b'floppyforms.fields.MultiValueField'), (b'SplitDateTimeField', b'floppyforms.fields.SplitDateTimeField')]),
            preserve_default=True,
        ),
    ]
