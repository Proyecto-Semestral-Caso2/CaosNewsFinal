# Generated by Django 4.2.1 on 2023-06-26 21:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0019_alter_noticia_autor_alter_noticia_categoria'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categorias',
            new_name='Categoria',
        ),
    ]
