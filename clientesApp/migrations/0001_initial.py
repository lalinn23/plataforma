# Generated by Django 5.0.2 on 2024-02-25 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreC', models.CharField(max_length=250, unique=True)),
                ('published', models.BooleanField(default=False)),
            ],
        ),
    ]
