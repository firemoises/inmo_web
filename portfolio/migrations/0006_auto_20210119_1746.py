# Generated by Django 3.1.2 on 2021-01-19 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_auto_20210119_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inmueble',
            name='gas',
            field=models.IntegerField(choices=[(0, 'Sin gas comun'), (1, 'Gas comun sin medidor'), (2, 'Gas comun con medidor')], default=0, verbose_name='Gas comun'),
        ),
        migrations.AlterField(
            model_name='inmueble',
            name='planta',
            field=models.IntegerField(choices=[(0, 'Sin planta'), (1, 'Planta full'), (2, 'Planta solo areas comunes')], default=0, verbose_name='Planta electrica'),
        ),
    ]
