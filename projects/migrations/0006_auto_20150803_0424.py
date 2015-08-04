# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20150803_0317'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='short_description',
        ),
        migrations.AddField(
            model_name='project',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='info',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=10),
        ),
    ]
