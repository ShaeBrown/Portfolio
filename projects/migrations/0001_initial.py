# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('short_description', models.TextField(blank=True)),
                ('date', models.DateField()),
                ('in_development', models.BooleanField()),
                ('image', models.URLField()),
            ],
        ),
    ]
