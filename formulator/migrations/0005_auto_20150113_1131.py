# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields
import django_hstore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('formulator', '0004_auto_20150112_1848'),
    ]

    operations = [
        migrations.CreateModel(
            name='FieldSetTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('legend', models.CharField(max_length=200)),
                ('language_code', models.CharField(max_length=15, db_index=True)),
                ('master', models.ForeignKey(related_name='translations', editable=False, to='formulator.FieldSet', null=True)),
            ],
            options={
                'abstract': False,
                'db_table': 'formulator_fieldset_translation',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FieldTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(help_text='A verbose name for this field, for use in displaying this\n                                            field in a form. By default, Django will use a "pretty"\n                                            version of the form field name, if the Field is part of a\n                                            Form. ', max_length=200)),
                ('help_text', models.TextField(help_text="An optional string to use as 'help text' for this Field.", blank=True)),
                ('initial', models.CharField(help_text="A value to use in this Field's initial display. This value\n                                              is *not* used as a fallback if data isn't given. ", max_length=200, blank=True)),
                ('choices', django_hstore.fields.DictionaryField(null=True, blank=True)),
                ('language_code', models.CharField(max_length=15, db_index=True)),
                ('master', models.ForeignKey(related_name='translations', editable=False, to='formulator.Field', null=True)),
            ],
            options={
                'abstract': False,
                'db_table': 'formulator_field_translation',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='fieldtranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='fieldsettranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.RemoveField(
            model_name='field',
            name='choices',
        ),
        migrations.RemoveField(
            model_name='field',
            name='help_text',
        ),
        migrations.RemoveField(
            model_name='field',
            name='initial',
        ),
        migrations.RemoveField(
            model_name='field',
            name='label',
        ),
        migrations.RemoveField(
            model_name='fieldset',
            name='legend',
        ),
        migrations.AddField(
            model_name='field',
            name='name',
            field=models.CharField(default='', help_text='A short name to build the database field ', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fieldset',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=''),
            preserve_default=False,
        ),
    ]
