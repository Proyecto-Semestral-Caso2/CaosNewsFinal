# Generated by Django 4.2.1 on 2023-06-26 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0009_alter_noticia_categoria'),
    ]

    operations = [
        migrations.CreateModel(
            name='Revisar_Noticia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(default='', max_length=30)),
                ('titulo', models.CharField(max_length=150)),
                ('subtitulo', models.CharField(max_length=250)),
                ('autor', models.CharField(max_length=10)),
                ('fecha', models.DateField()),
                ('cuerpo', models.TextField()),
                ('imagen', models.ImageField(null=True, upload_to='imagenes noticias en revision')),
                ('revision', models.TextField()),
            ],
        ),
    ]