# Generated by Django 2.0.8 on 2018-09-04 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0012_auto_20180904_1538'),
    ]

    operations = [
        migrations.RenameField(
            model_name='program',
            old_name='creationDate',
            new_name='creation_date',
        ),
        migrations.RenameField(
            model_name='program',
            old_name='hasCoupling',
            new_name='has_coupling',
        ),
        migrations.RenameField(
            model_name='program',
            old_name='programInterval',
            new_name='program_interval',
        ),
        migrations.RenameField(
            model_name='program',
            old_name='registerInterval',
            new_name='register_interval',
        ),
        migrations.RemoveField(
            model_name='program',
            name='isPublic',
        ),
    ]
