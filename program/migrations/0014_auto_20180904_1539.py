# Generated by Django 2.0.8 on 2018-09-04 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0013_auto_20180904_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
