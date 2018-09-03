# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2018-09-03 14:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20161010_1231'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='conscription',
            field=models.CharField(choices=[('went', 'دارای کارت پایان خدمت'), ('exempt', 'معافیت دایم '), ('educational exempt', 'معافیت تحصیلی'), ('army', 'نظامی'), ('respite', 'مهلت قانونی معرفی'), ('other', 'سایر')], max_length=200, verbose_name='وضعیت نظام وظیفه'),
        ),
    ]
