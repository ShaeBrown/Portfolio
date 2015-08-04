# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_auto_20150803_0936'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='download_url',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='source_type',
            field=models.CharField(default='', max_length=200, choices=[('<i class="icon-gamemaker"></i> <span class="network-name">Get source as GMK</span></a>', 'GMK'), ('<i class="fa fa-github fa-fw"></i> <span class="network-name">Get source on Github</span></a>', 'GITHUB')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='source_url',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
    ]
