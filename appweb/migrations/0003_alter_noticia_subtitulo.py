# Generated by Django 4.2.1 on 2023-06-21 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0002_alter_noticia_subtitulo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='subtitulo',
            field=models.TextField(max_length=100),
        ),
    ]
