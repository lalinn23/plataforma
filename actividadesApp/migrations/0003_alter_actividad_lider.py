# Generated by Django 5.0.2 on 2024-03-18 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actividadesApp', '0002_alter_actividad_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividad',
            name='lider',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
    ]
