# Generated by Django 4.2.1 on 2023-07-14 01:46

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0038_alter_postulacion_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='imagen',
            field=models.ImageField(null=True, upload_to='imagenes_noticias'),
        ),
        migrations.AlterField(
            model_name='postulacion',
            name='descripcion',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]
