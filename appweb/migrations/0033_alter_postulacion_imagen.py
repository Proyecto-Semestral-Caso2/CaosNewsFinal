# Generated by Django 4.2.1 on 2023-07-06 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0032_alter_postulacion_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postulacion',
            name='imagen',
            field=models.ImageField(null=True, upload_to='imagenes_postulantes'),
        ),
    ]
