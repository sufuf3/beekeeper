# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-07 08:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='build',
            options={'ordering': ('-updated',)},
        ),
        migrations.AlterModelOptions(
            name='change',
            options={'ordering': ('project__repository__name', '-updated')},
        ),
        migrations.AlterField(
            model_name='build',
            name='status',
            field=models.IntegerField(choices=[(10, 'Created'), (20, 'Running'), (100, 'Done'), (200, 'Error'), (9998, 'Stopping'), (9999, 'Stopped')], default=10),
        ),
    ]
