# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-11 04:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0006_auto_20171011_0142'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='isbn',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
