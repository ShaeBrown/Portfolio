# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_project_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='tags',
            field=models.CharField(max_length=2, default=None, choices=[('Programming', (('py', 'Python'), ('ja', 'Java'), ('c', 'C'))), ('Game Engines', (('gm', 'Game Maker'), ('cry', 'CryEngine')))]),
        ),
    ]
