# Generated by Django 4.2.1 on 2023-07-09 19:47

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0035_alter_autor_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='descripcion',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]
