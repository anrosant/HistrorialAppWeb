# Generated by Django 2.0.6 on 2018-06-23 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('historial', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=16)),
                ('contrasenia', models.CharField(max_length=16)),
            ],
        ),
    ]
