# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-01 15:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20171206_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='day',
            field=models.DateField(default=datetime.datetime(2018, 3, 1, 15, 23, 19, 908294)),
        ),
    ]