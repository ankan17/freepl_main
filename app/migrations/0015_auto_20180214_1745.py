# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-14 17:45
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20180210_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='day',
            field=models.DateField(default=datetime.datetime(2018, 2, 14, 17, 45, 13, 17753)),
        ),
    ]
