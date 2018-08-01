# Generated by Django 2.0 on 2018-07-31 23:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20180731_0314'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='ficha_actual',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='atencionenfermeria',
            name='fechaAtencion',
            field=models.DateField(default=datetime.datetime(2018, 7, 31, 23, 41, 36, 3496, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='consultamedica',
            name='fechaConsulta',
            field=models.DateField(default=datetime.datetime(2018, 7, 31, 23, 41, 36, 2672, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2018, 7, 31, 23, 41, 36, 1055, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='permisomedico',
            name='fecha_fin',
            field=models.DateField(default=datetime.datetime(2018, 7, 31, 23, 41, 36, 6384, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='permisomedico',
            name='fecha_inicio',
            field=models.DateField(default=datetime.datetime(2018, 7, 31, 23, 41, 36, 6349, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='signosvitales',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2018, 7, 31, 23, 41, 36, 4274, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='vacuna',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2018, 7, 31, 23, 41, 36, 7744, tzinfo=utc)),
        ),
    ]