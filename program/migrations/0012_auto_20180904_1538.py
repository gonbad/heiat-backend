# Generated by Django 2.0.8 on 2018-09-04 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0011_auto_20180904_1533'),
    ]

    operations = [
        migrations.RenameField(
            model_name='program',
            old_name='isOpen',
            new_name='is_open',
        ),
        migrations.RemoveField(
            model_name='program',
            name='additionalOption',
        ),
    ]
