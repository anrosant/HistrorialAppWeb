# Generated by Django 2.0 on 2018-07-31 03:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20180730_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atencionenfermeria',
            name='fechaAtencion',
            field=models.DateField(default=datetime.datetime(2018, 7, 31, 3, 14, 25, 393246, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='consultamedica',
            name='fechaConsulta',
            field=models.DateField(default=datetime.datetime(2018, 7, 31, 3, 14, 25, 392471, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2018, 7, 31, 3, 14, 25, 390928, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='permisomedico',
            name='fecha_fin',
            field=models.DateField(default=datetime.datetime(2018, 7, 31, 3, 14, 25, 396077, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='permisomedico',
            name='fecha_inicio',
            field=models.DateField(default=datetime.datetime(2018, 7, 31, 3, 14, 25, 396044, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='signosvitales',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2018, 7, 31, 3, 14, 25, 394066, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='vacuna',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2018, 7, 31, 3, 14, 25, 397379, tzinfo=utc)),
        ),
    ]
