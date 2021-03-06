# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-08-03 11:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('router', '0009_ip_ms'),
    ]

    operations = [
        migrations.CreateModel(
            name='Error',
            fields=[
                ('error_id', models.AutoField(primary_key=True, serialize=False)),
                ('host', models.CharField(max_length=20)),
                ('time', models.CharField(max_length=20)),
                ('text', models.CharField(max_length=1000, null=True)),
                ('msg', models.CharField(max_length=2000, null=True)),
                ('status', models.CharField(default='1', max_length=10)),
                ('mail', models.CharField(max_length=10, null=True)),
                ('distribution', models.CharField(max_length=10, null=True)),
                ('run', models.CharField(max_length=10, null=True)),
            ],
        ),
    ]
