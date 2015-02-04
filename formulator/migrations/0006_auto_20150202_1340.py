# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('formulator', '0005_auto_20150113_1131'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fieldset',
            options={'ordering': ['position']},
        ),
        migrations.AlterField(
            model_name='field',
            name='required',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='fieldset',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False),
            preserve_default=True,
        ),
    ]
