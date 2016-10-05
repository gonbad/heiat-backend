# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-10-05 08:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20161005_0813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.CharField(max_length=400, null=True, verbose_name='آدرس'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='cellPhone',
            field=models.CharField(max_length=11, null=True, verbose_name='شماره موبایل'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='couple',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Profile', verbose_name='همسر'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='emergencyPhone',
            field=models.CharField(max_length=20, null=True, verbose_name='شماره تلفن ضروری'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='fatherName',
            field=models.CharField(max_length=200, null=True, verbose_name='نام پدر'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='shenasname',
            field=models.CharField(max_length=11, null=True, verbose_name='شماره شناسنامه'),
        ),
    ]