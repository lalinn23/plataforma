# Generated by Django 5.0.2 on 2024-03-14 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actividadesApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividad',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]