# Generated by Django 4.0.4 on 2022-06-18 23:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mtaani', '0004_rename_admin_neighbourhood_neighbourhood_admin_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='Neighbourhood',
            new_name='neighbourhood',
        ),
    ]