# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-25 01:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0003_auto_20160423_0502'),
    ]

    operations = [
        migrations.CreateModel(
            name='CachedTransaction',
            fields=[
                ('txid', models.CharField(max_length=72, primary_key=True, serialize=False)),
                ('content', models.TextField()),
            ],
        ),
    ]
