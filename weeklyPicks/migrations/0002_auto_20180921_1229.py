# Generated by Django 2.1.1 on 2018-09-21 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weeklyPicks', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Football',
            new_name='Pick',
        ),
        migrations.RenameModel(
            old_name='Teams',
            new_name='Team',
        ),
    ]
