# Generated by Django 2.0.8 on 2018-09-04 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0015_auto_20180904_1540'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='additionalOption',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='feedBack',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='label1',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='label2',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='label3',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='label4',
        ),
    ]
