# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-30 11:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20170430_1825'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='createtime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='updatetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
