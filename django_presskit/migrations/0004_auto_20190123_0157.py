# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-01-23 01:57
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.deletion
import filer.fields.file


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0010_auto_20180414_2058'),
        ('django_presskit', '0003_auto_20181002_1915'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='asset_archive',
            field=filer.fields.file.FilerFileField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='filer.File'),
        ),
        migrations.AddField(
            model_name='project',
            name='asset_archive',
            field=filer.fields.file.FilerFileField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='filer.File'),
        ),
    ]
