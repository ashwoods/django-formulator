# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('formulator', '0002_field_choices'),
    ]

    operations = [
        migrations.RenameField(
            model_name='field',
            old_name='formset',
            new_name='fieldset',
        ),
        migrations.RemoveField(
            model_name='field',
            name='name',
        ),
        migrations.AddField(
            model_name='field',
            name='maxlength',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='field',
            name='field',
            field=models.CharField(max_length=100, choices=[(b'Field', b'Field'), (b'CharField', b'CharField'), (b'IntegerField', b'IntegerField'), (b'DateField', b'DateField'), (b'TimeField', b'TimeField'), (b'DateTimeField', b'DateTimeField'), (b'EmailField', b'EmailField'), (b'FileField', b'FileField'), (b'ImageField', b'ImageField'), (b'URLField', b'URLField'), (b'BooleanField', b'BooleanField'), (b'NullBooleanField', b'NullBooleanField'), (b'ChoiceField', b'ChoiceField'), (b'MultipleChoiceField', b'MultipleChoiceField'), (b'FloatField', b'FloatField'), (b'DecimalField', b'DecimalField'), (b'SlugField', b'SlugField'), (b'RegexField', b'RegexField'), (b'IPAddressField', b'IPAddressField'), (b'GenericIPAddressField', b'GenericIPAddressField'), (b'TypedChoiceField', b'TypedChoiceField'), (b'FilePathField', b'FilePathField'), (b'TypedMultipleChoiceField', b'TypedMultipleChoiceField'), (b'ComboField', b'ComboField'), (b'MultiValueField', b'MultiValueField'), (b'SplitDateTimeField', b'SplitDateTimeField')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='field',
            name='field_id',
            field=autoslug.fields.AutoSlugField(editable=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='field',
            name='label',
            field=models.CharField(help_text='A verbose name for this field, for use in displaying this\n                                            field in a form. By default, Django will use a "pretty"\n                                            version of the form field name, if the Field is part of a\n                                            Form. ', max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='form',
            name='form_method',
            field=models.IntegerField(default=1, max_length=10, choices=[(0, 'GET'), (1, 'POST')]),
            preserve_default=True,
        ),
    ]
