# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_hstore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('formulator', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='field',
            name='choices',
            field=django_hstore.fields.DictionaryField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
