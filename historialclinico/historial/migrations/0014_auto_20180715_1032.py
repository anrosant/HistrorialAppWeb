# Generated by Django 2.0.6 on 2018-07-15 15:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('historial', '0013_auto_20180715_1030'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signosvitales',
            name='examen_fisico',
        ),
        migrations.AlterField(
            model_name='atencionenfermeria',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2018, 7, 15, 15, 32, 49, 882326, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='chequeo',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2018, 7, 15, 15, 32, 49, 884331, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='consultamedica',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2018, 7, 15, 15, 32, 49, 881323, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='fecha_nacimiento',
            field=models.DateField(default=datetime.datetime(2018, 7, 15, 15, 32, 49, 881323, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='fecha_registro',
            field=models.DateField(default=datetime.datetime(2018, 7, 15, 15, 32, 49, 881323, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='inmunizacion',
            name='fecha_aplicacion',
            field=models.DateField(default=datetime.datetime(2018, 7, 15, 15, 32, 49, 887342, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='permisomedico',
            name='fecha_fin',
            field=models.DateField(default=datetime.datetime(2018, 7, 15, 15, 32, 49, 883328, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='permisomedico',
            name='fecha_inicio',
            field=models.DateField(default=datetime.datetime(2018, 7, 15, 15, 32, 49, 883328, tzinfo=utc)),
        ),
    ]