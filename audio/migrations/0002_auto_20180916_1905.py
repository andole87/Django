# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-16 10:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='audio',
            old_name='audisrc',
            new_name='audiosrc',
        ),
    ]
