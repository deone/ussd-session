# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-16 21:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('session', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='actor_first_name',
            field=models.CharField(default='A', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='session',
            name='actor_last_name',
            field=models.CharField(default='A', max_length=20),
            preserve_default=False,
        ),
    ]
