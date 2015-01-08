# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields
import django_hstore.fields
import positions.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('position', positions.fields.PositionField(default=-1)),
                ('field', models.CharField(max_length=100, choices=[(b'Field', b'floppyforms.fields.Field'), (b'CharField', b'floppyforms.fields.CharField'), (b'IntegerField', b'floppyforms.fields.IntegerField'), (b'DateField', b'floppyforms.fields.DateField'), (b'TimeField', b'floppyforms.fields.TimeField'), (b'DateTimeField', b'floppyforms.fields.DateTimeField'), (b'EmailField', b'floppyforms.fields.EmailField'), (b'FileField', b'floppyforms.fields.FileField'), (b'ImageField', b'floppyforms.fields.ImageField'), (b'URLField', b'floppyforms.fields.URLField'), (b'BooleanField', b'floppyforms.fields.BooleanField'), (b'NullBooleanField', b'floppyforms.fields.NullBooleanField'), (b'ChoiceField', b'floppyforms.fields.ChoiceField'), (b'MultipleChoiceField', b'floppyforms.fields.MultipleChoiceField'), (b'FloatField', b'floppyforms.fields.FloatField'), (b'DecimalField', b'floppyforms.fields.DecimalField'), (b'SlugField', b'floppyforms.fields.SlugField'), (b'RegexField', b'floppyforms.fields.RegexField'), (b'IPAddressField', b'floppyforms.fields.IPAddressField'), (b'GenericIPAddressField', b'floppyforms.fields.GenericIPAddressField'), (b'TypedChoiceField', b'floppyforms.fields.TypedChoiceField'), (b'FilePathField', b'floppyforms.fields.FilePathField'), (b'TypedMultipleChoiceField', b'floppyforms.fields.TypedMultipleChoiceField'), (b'ComboField', b'floppyforms.fields.ComboField'), (b'MultiValueField', b'floppyforms.fields.MultiValueField'), (b'SplitDateTimeField', b'floppyforms.fields.SplitDateTimeField')])),
                ('attrs', django_hstore.fields.DictionaryField(null=True, blank=True)),
                ('field_id', autoslug.fields.AutoSlugField(unique=True, editable=False)),
                ('required', models.BooleanField(default=True, help_text='Boolean that specifies whether the field is required.')),
                ('widget', models.CharField(blank=True, help_text="A Widget class, or instance of a Widget class, that should\n                                           be used for this Field when displaying it. Each Field has a\n                                           default Widget that it'll use if you don't specify this. In\n                                           most cases, the default widget is TextInput.", max_length=100, choices=[(b'TextInput', b'floppyforms.widgets.TextInput'), (b'PasswordInput', b'floppyforms.widgets.PasswordInput'), (b'HiddenInput', b'floppyforms.widgets.HiddenInput'), (b'ClearableFileInput', b'floppyforms.widgets.ClearableFileInput'), (b'FileInput', b'floppyforms.widgets.FileInput'), (b'DateInput', b'floppyforms.widgets.DateInput'), (b'DateTimeInput', b'floppyforms.widgets.DateTimeInput'), (b'TimeInput', b'floppyforms.widgets.TimeInput'), (b'Textarea', b'floppyforms.widgets.Textarea'), (b'CheckboxInput', b'floppyforms.widgets.CheckboxInput'), (b'Select', b'floppyforms.widgets.Select'), (b'NullBooleanSelect', b'floppyforms.widgets.NullBooleanSelect'), (b'SelectMultiple', b'floppyforms.widgets.SelectMultiple'), (b'RadioSelect', b'floppyforms.widgets.RadioSelect'), (b'CheckboxSelectMultiple', b'floppyforms.widgets.CheckboxSelectMultiple'), (b'SearchInput', b'floppyforms.widgets.SearchInput'), (b'RangeInput', b'floppyforms.widgets.RangeInput'), (b'ColorInput', b'floppyforms.widgets.ColorInput'), (b'EmailInput', b'floppyforms.widgets.EmailInput'), (b'URLInput', b'floppyforms.widgets.URLInput'), (b'PhoneNumberInput', b'floppyforms.widgets.PhoneNumberInput'), (b'NumberInput', b'floppyforms.widgets.NumberInput'), (b'IPAddressInput', b'floppyforms.widgets.IPAddressInput'), (b'MultiWidget', b'floppyforms.widgets.MultiWidget'), (b'Widget', b'floppyforms.widgets.Widget'), (b'SplitDateTimeWidget', b'floppyforms.widgets.SplitDateTimeWidget'), (b'SplitHiddenDateTimeWidget', b'floppyforms.widgets.SplitHiddenDateTimeWidget'), (b'MultipleHiddenInput', b'floppyforms.widgets.MultipleHiddenInput'), (b'SelectDateWidget', b'floppyforms.widgets.SelectDateWidget'), (b'SlugInput', b'floppyforms.widgets.SlugInput')])),
                ('label', models.CharField(help_text='A verbose name for this field, for use in displaying this\n                                            field in a form. By default, Django will use a "pretty"\n                                            version of the form field name, if the Field is part of a\n                                            Form. ', max_length=100, blank=True)),
                ('initial', models.CharField(help_text="A value to use in this Field's initial display. This value\n                                              is *not* used as a fallback if data isn't given. ", max_length=200, blank=True)),
                ('help_text', models.TextField(help_text="An optional string to use as 'help text' for this Field.", blank=True)),
                ('show_hidden_initial', models.BooleanField(default=False, help_text='Boolean that specifies whether the field is hidden.')),
                ('repeat_min', models.IntegerField(default=1, help_text='The minimum number of times this Field should appear in the Form')),
                ('repeat_max', models.IntegerField(help_text='The maximum number of times this Field should appear in the Form', null=True, blank=True)),
            ],
            options={
                'ordering': ['position'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FieldSet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('position', positions.fields.PositionField(default=-1)),
                ('name', models.CharField(max_length=100)),
                ('legend', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='Name of the Form type', max_length=100)),
                ('form_name', models.CharField(max_length=100, blank=True)),
                ('form_action', models.CharField(max_length=250, blank=True)),
                ('form_method', models.IntegerField(default=0, max_length=10, choices=[(0, 'GET'), (1, 'POST')])),
                ('form_id', autoslug.fields.AutoSlugField(unique=True, editable=False)),
                ('form_class', models.CharField(max_length=250, blank=True)),
                ('form_accept_charset', models.CharField(max_length=100, blank=True)),
                ('form_autocomplete', models.BooleanField(default=False)),
                ('form_novalidate', models.BooleanField(default=False)),
                ('form_enctype', models.IntegerField(default=0, choices=[(0, 'application/x-www-form-urlencoded'), (1, 'multipart/form-data'), (2, 'text/plain')])),
                ('form_target', models.CharField(max_length=50, blank=True)),
                ('attrs', django_hstore.fields.DictionaryField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='fieldset',
            name='form',
            field=models.ForeignKey(to='formulator.Form'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='field',
            name='formset',
            field=models.ForeignKey(to='formulator.FieldSet'),
            preserve_default=True,
        ),
    ]
