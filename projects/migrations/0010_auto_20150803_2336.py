# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_auto_20150803_2314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='download_url',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]
