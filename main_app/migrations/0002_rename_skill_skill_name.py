# Generated by Django 4.0.1 on 2022-01-17 19:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skill',
            old_name='skill',
            new_name='name',
        ),
    ]
