# Generated by Django 3.2.3 on 2021-06-05 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('patente', models.CharField(max_length=6, primary_key=True, serialize=False, verbose_name='Patente')),
                ('marca', models.CharField(max_length=20, verbose_name='Marca')),
                ('modelo', models.CharField(max_length=20, verbose_name='Modelo')),
            ],
        ),
    ]
