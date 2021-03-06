# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-05 10:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=10)),
                ('session_id', models.CharField(max_length=40)),
                ('service_code', models.CharField(max_length=15)),
                ('operator', models.CharField(max_length=10)),
                ('initiation_message', models.CharField(max_length=15)),
                ('succeeded', models.BooleanField(default=False)),
                ('menu_option', models.PositiveSmallIntegerField(null=True)),
                ('sequence_at_menu', models.PositiveSmallIntegerField(null=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('action', models.CharField(max_length=30, null=True)),
                ('method', models.CharField(max_length=50, null=True)),
                ('step_at_paged', models.PositiveSmallIntegerField(null=True)),
                ('page_stop', models.PositiveSmallIntegerField(null=True)),
                ('selector', models.PositiveSmallIntegerField(null=True)),
            ],
        ),
    ]
