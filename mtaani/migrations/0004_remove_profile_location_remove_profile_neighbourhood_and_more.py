# Generated by Django 4.0.4 on 2022-06-20 02:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mtaani', '0003_alter_neighbourhood_neighbourhood_admin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='location',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='neighbourhood',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='profile_name',
        ),
    ]
