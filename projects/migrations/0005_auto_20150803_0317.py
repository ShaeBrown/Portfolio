# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20150803_0316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='tags',
            field=models.CharField(default=None, max_length=100, choices=[('Programming', (('<a class="btn btn-tag" href="#"><i class="devicon-python-plain"></i>Python</a>', 'Python'), ('ja', 'Java'), ('c', 'C'))), ('Game Engines', (('gm', 'Game Maker'), ('cry', 'CryEngine')))]),
        ),
    ]
