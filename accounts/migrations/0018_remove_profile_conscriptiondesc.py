# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2018-09-04 09:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_auto_20180904_0927'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='conscriptionDesc',
        ),
    ]