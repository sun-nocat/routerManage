# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-07-23 06:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('router', '0007_auto_20180722_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='ip',
            name='times',
            field=models.CharField(max_length=20, null=True),
        ),
    ]