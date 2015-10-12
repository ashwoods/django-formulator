# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import model_utils.fields
import autoslug.fields
import django.utils.timezone
import positions.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Choices',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('key', models.CharField(max_length=100)),
                ('value', models.CharField(max_length=100, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('label', models.CharField(help_text='A verbose name for this field, for use in displaying this\n                                        field in a form. By default, Django will use a "pretty"\n                                        version of the form field name, if the Field is part of a\n                                        Form. ', max_length=200)),
                ('name', models.CharField(help_text='A short name to build the database field ', max_length=200)),
                ('field_id', autoslug.fields.AutoSlugField(populate_from='name', unique_with=('form',), editable=False)),
                ('position', positions.fields.PositionField(default=-1)),
                ('field_type', models.CharField(max_length=100, choices=[(b'floppyforms.fields.Field', b'Field'), (b'floppyforms.fields.CharField', b'CharField'), (b'floppyforms.fields.IntegerField', b'IntegerField'), (b'floppyforms.fields.DateField', b'DateField'), (b'floppyforms.fields.TimeField', b'TimeField'), (b'floppyforms.fields.DateTimeField', b'DateTimeField'), (b'floppyforms.fields.EmailField', b'EmailField'), (b'floppyforms.fields.FileField', b'FileField'), (b'floppyforms.fields.ImageField', b'ImageField'), (b'floppyforms.fields.URLField', b'URLField'), (b'floppyforms.fields.BooleanField', b'BooleanField'), (b'floppyforms.fields.NullBooleanField', b'NullBooleanField'), (b'floppyforms.fields.ChoiceField', b'ChoiceField'), (b'floppyforms.fields.MultipleChoiceField', b'MultipleChoiceField'), (b'floppyforms.fields.FloatField', b'FloatField'), (b'floppyforms.fields.DecimalField', b'DecimalField'), (b'floppyforms.fields.SlugField', b'SlugField'), (b'floppyforms.fields.RegexField', b'RegexField'), (b'floppyforms.fields.IPAddressField', b'IPAddressField'), (b'floppyforms.fields.GenericIPAddressField', b'GenericIPAddressField'), (b'floppyforms.fields.TypedChoiceField', b'TypedChoiceField'), (b'floppyforms.fields.FilePathField', b'FilePathField'), (b'floppyforms.fields.TypedMultipleChoiceField', b'TypedMultipleChoiceField'), (b'floppyforms.fields.ComboField', b'ComboField'), (b'floppyforms.fields.MultiValueField', b'MultiValueField'), (b'floppyforms.fields.SplitDateTimeField', b'SplitDateTimeField')])),
                ('max_length', models.IntegerField(null=True, blank=True)),
                ('placeholder', models.CharField(max_length=255, blank=True)),
                ('required', models.BooleanField(default=True)),
                ('help_text', models.TextField(help_text="An optional string to use as 'help text' for this Field.", blank=True)),
                ('initial', models.CharField(help_text="A value to use in this Field's initial display. This value\n                                          is *not* used as a fallback if data isn't given. ", max_length=200, blank=True)),
                ('widget', models.CharField(blank=True, help_text="A Widget class, or instance of a Widget class, that should\n                                           be used for this Field when displaying it. Each Field has a\n                                           default Widget that it'll use if you don't specify this. In\n                                           most cases, the default widget is TextInput.", max_length=100, choices=[(b'floppyforms.widgets.TextInput', b'TextInput'), (b'floppyforms.widgets.PasswordInput', b'PasswordInput'), (b'floppyforms.widgets.HiddenInput', b'HiddenInput'), (b'floppyforms.widgets.ClearableFileInput', b'ClearableFileInput'), (b'floppyforms.widgets.FileInput', b'FileInput'), (b'floppyforms.widgets.DateInput', b'DateInput'), (b'floppyforms.widgets.DateTimeInput', b'DateTimeInput'), (b'floppyforms.widgets.TimeInput', b'TimeInput'), (b'floppyforms.widgets.Textarea', b'Textarea'), (b'floppyforms.widgets.CheckboxInput', b'CheckboxInput'), (b'floppyforms.widgets.Select', b'Select'), (b'floppyforms.widgets.NullBooleanSelect', b'NullBooleanSelect'), (b'floppyforms.widgets.SelectMultiple', b'SelectMultiple'), (b'floppyforms.widgets.RadioSelect', b'RadioSelect'), (b'floppyforms.widgets.CheckboxSelectMultiple', b'CheckboxSelectMultiple'), (b'floppyforms.widgets.SearchInput', b'SearchInput'), (b'floppyforms.widgets.RangeInput', b'RangeInput'), (b'floppyforms.widgets.ColorInput', b'ColorInput'), (b'floppyforms.widgets.EmailInput', b'EmailInput'), (b'floppyforms.widgets.URLInput', b'URLInput'), (b'floppyforms.widgets.PhoneNumberInput', b'PhoneNumberInput'), (b'floppyforms.widgets.NumberInput', b'NumberInput'), (b'floppyforms.widgets.IPAddressInput', b'IPAddressInput'), (b'floppyforms.widgets.MultiWidget', b'MultiWidget'), (b'floppyforms.widgets.Widget', b'Widget'), (b'floppyforms.widgets.SplitDateTimeWidget', b'SplitDateTimeWidget'), (b'floppyforms.widgets.SplitHiddenDateTimeWidget', b'SplitHiddenDateTimeWidget'), (b'floppyforms.widgets.MultipleHiddenInput', b'MultipleHiddenInput'), (b'floppyforms.widgets.SelectDateWidget', b'SelectDateWidget'), (b'floppyforms.widgets.SlugInput', b'SlugInput')])),
                ('show_hidden_initial', models.BooleanField(default=False, help_text='Boolean that specifies whether the field is hidden.')),
            ],
            options={
                'ordering': ['form', 'position'],
            },
        ),
        migrations.CreateModel(
            name='FieldAttribute',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('key', models.CharField(max_length=100)),
                ('value', models.CharField(max_length=100, blank=True)),
                ('field', models.ForeignKey(to='formulator.Field')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FieldSet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('position', positions.fields.PositionField(default=-1)),
                ('name', models.CharField(max_length=100)),
                ('legend', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['form', 'position'],
            },
        ),
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('name', models.CharField(help_text='Name of the Form type', max_length=100)),
                ('form_name', models.CharField(max_length=100, blank=True)),
                ('form_action', models.CharField(max_length=250, blank=True)),
                ('form_method', models.IntegerField(default=1, choices=[(0, 'GET'), (1, 'POST')])),
                ('form_id', autoslug.fields.AutoSlugField(populate_from='name', editable=False)),
                ('form_class', models.CharField(max_length=250, blank=True)),
                ('form_accept_charset', models.CharField(max_length=100, blank=True)),
                ('form_autocomplete', models.BooleanField(default=False)),
                ('form_novalidate', models.BooleanField(default=False)),
                ('form_enctype', models.IntegerField(default=0, choices=[(0, 'application/x-www-form-urlencoded'), (1, 'multipart/form-data'), (2, 'text/plain')])),
                ('form_target', models.CharField(max_length=50, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WidgetAttribute',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('key', models.CharField(max_length=100)),
                ('value', models.CharField(max_length=100)),
                ('field', models.ForeignKey(to='formulator.Field')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='fieldset',
            name='form',
            field=models.ForeignKey(to='formulator.Form'),
        ),
        migrations.AddField(
            model_name='field',
            name='fieldset',
            field=models.ForeignKey(to='formulator.FieldSet', null=True),
        ),
        migrations.AddField(
            model_name='field',
            name='form',
            field=models.ForeignKey(to='formulator.Form'),
        ),
        migrations.AddField(
            model_name='choices',
            name='field',
            field=models.ForeignKey(to='formulator.Field'),
        ),
        migrations.AlterOrderWithRespectTo(
            name='field',
            order_with_respect_to='form',
        ),
    ]
