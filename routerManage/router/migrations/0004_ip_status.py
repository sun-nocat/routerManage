# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-07-22 07:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('router', '0003_auto_20180722_1332'),
    ]

    operations = [
        migrations.AddField(
            model_name='ip',
            name='status',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
