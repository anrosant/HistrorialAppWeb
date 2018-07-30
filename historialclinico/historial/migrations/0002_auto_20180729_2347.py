# Generated by Django 2.1rc1 on 2018-07-30 04:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('historial', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atencionenfermeria',
            name='fechaAtencion',
            field=models.DateField(default=datetime.datetime(2018, 7, 30, 4, 47, 19, 26447, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='consultamedica',
            name='fechaConsulta',
            field=models.DateField(default=datetime.datetime(2018, 7, 30, 4, 47, 19, 26447, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='edad',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2018, 7, 30, 4, 47, 19, 26447, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='permisomedico',
            name='fecha_fin',
            field=models.DateField(default=datetime.datetime(2018, 7, 30, 4, 47, 19, 26447, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='permisomedico',
            name='fecha_inicio',
            field=models.DateField(default=datetime.datetime(2018, 7, 30, 4, 47, 19, 26447, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='signosvitales',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2018, 7, 30, 4, 47, 19, 26447, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='vacuna',
            name='dosis',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='vacuna',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2018, 7, 30, 4, 47, 19, 26447, tzinfo=utc)),
        ),
    ]