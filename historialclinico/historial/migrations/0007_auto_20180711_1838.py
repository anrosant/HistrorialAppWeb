# Generated by Django 2.0.6 on 2018-07-11 23:38

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('historial', '0006_auto_20180711_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atencionenfermeria',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2018, 7, 11, 23, 38, 46, 77297, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='chequeo',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2018, 7, 11, 23, 38, 46, 83313, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='consultamedica',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2018, 7, 11, 23, 38, 46, 76294, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='fecha_nacimiento',
            field=models.DateField(default=datetime.datetime(2018, 7, 11, 23, 38, 46, 75291, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='fecha_registro',
            field=models.DateField(default=datetime.datetime(2018, 7, 11, 23, 38, 46, 75291, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='inmunizacion',
            name='fecha_aplicacion',
            field=models.DateField(default=datetime.datetime(2018, 7, 11, 23, 38, 46, 91334, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='permisomedico',
            name='fecha_fin',
            field=models.DateField(default=datetime.datetime(2018, 7, 11, 23, 38, 46, 80305, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='permisomedico',
            name='fecha_inicio',
            field=models.DateField(default=datetime.datetime(2018, 7, 11, 23, 38, 46, 80305, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='signosvitales',
            name='consulta_medica',
            field=models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='historial.ConsultaMedica'),
        ),
    ]
