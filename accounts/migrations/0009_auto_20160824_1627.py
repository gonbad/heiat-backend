# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-24 11:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20160824_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='passport_dateofexpiry',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='passport_dateofissue',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='passport_number',
            field=models.IntegerField(null=True),
        ),
    ]
