# Generated by Django 4.0.4 on 2022-06-20 02:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mtaani', '0002_alter_post_post_neighbourhood_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='neighbourhood',
            name='neighbourhood_admin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hood', to=settings.AUTH_USER_MODEL),
        ),
    ]
