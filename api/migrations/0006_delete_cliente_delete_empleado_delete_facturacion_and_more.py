# Generated by Django 4.0.4 on 2023-05-25 01:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_bandejatrabajo_fechaot'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cliente',
        ),
        migrations.DeleteModel(
            name='Empleado',
        ),
        migrations.DeleteModel(
            name='Facturacion',
        ),
        migrations.DeleteModel(
            name='Ot',
        ),
        migrations.DeleteModel(
            name='Productos',
        ),
        migrations.DeleteModel(
            name='Proveedor',
        ),
        migrations.DeleteModel(
            name='Servicio',
        ),
        migrations.DeleteModel(
            name='Vehiculos',
        ),
    ]
