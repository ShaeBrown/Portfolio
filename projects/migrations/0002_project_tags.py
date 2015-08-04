# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='tags',
            field=models.CharField(choices=[('Programming', (('python', 'Python'), ('java', 'Java'))), ('Game Engines', (('gm', 'Game Maker'), ('cry', 'CryEngine')))], max_length=2, default=None),
        ),
    ]
