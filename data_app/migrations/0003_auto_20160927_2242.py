# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-27 22:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_app', '0002_auto_20160927_2203'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customers',
            old_name='zip',
            new_name='zip_code',
        ),
    ]
