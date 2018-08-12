# Generated by Django 2.0 on 2018-08-10 23:50

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20180810_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atencionenfermeria',
            name='fechaAtencion',
            field=models.DateField(default=datetime.datetime(2018, 8, 10, 23, 50, 40, 229113, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='consultamedica',
            name='fechaConsulta',
            field=models.DateField(default=datetime.datetime(2018, 8, 10, 23, 50, 40, 227155, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='diagnostico',
            name='consulta_medica',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.ConsultaMedica'),
        ),
        migrations.AlterField(
            model_name='diagnostico',
            name='enfermedad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Enfermedad'),
        ),
        migrations.AlterField(
            model_name='diagnostico',
            name='permiso_medico',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.PermisoMedico'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2018, 8, 10, 23, 50, 40, 219414, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='permisomedico',
            name='fecha_fin',
            field=models.DateField(default=datetime.datetime(2018, 8, 10, 23, 50, 40, 233182, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='permisomedico',
            name='fecha_inicio',
            field=models.DateField(default=datetime.datetime(2018, 8, 10, 23, 50, 40, 233113, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='signosvitales',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2018, 8, 10, 23, 50, 40, 230387, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='vacuna',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2018, 8, 10, 23, 50, 40, 237056, tzinfo=utc)),
        ),
    ]