# Generated by Django 4.2.1 on 2023-07-06 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0031_remove_postulacion_fecha_postulacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postulacion',
            name='imagen',
            field=models.FileField(null=True, upload_to='imagenes_postulantes'),
        ),
    ]