# Generated by Django 4.0.1 on 2022-01-19 00:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_rename_skill_skill_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 1, 19, 0, 56, 1, 154086)),
        ),
        migrations.AddField(
            model_name='resume',
            name='name',
            field=models.CharField(default='Resume', max_length=200),
            preserve_default=False,
        ),
    ]