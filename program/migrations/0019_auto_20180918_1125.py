# Generated by Django 2.0.8 on 2018-09-18 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0018_auto_20180916_1445'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='management',
            name='profile',
        ),
        migrations.RemoveField(
            model_name='management',
            name='program',
        ),
        migrations.DeleteModel(
            name='Management',
        ),
    ]