# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20150722_2156'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='featured',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='tags',
            field=models.CharField(max_length=2, choices=[('Programming', (('<a class="btn btn-tag" href="#"><i class="devicon-python-plain"></i>Python</a>', 'Python'), ('ja', 'Java'), ('c', 'C'))), ('Game Engines', (('gm', 'Game Maker'), ('cry', 'CryEngine')))], default=None),
        ),
    ]
