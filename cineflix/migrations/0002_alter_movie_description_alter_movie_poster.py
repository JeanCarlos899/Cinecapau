# Generated by Django 4.0.5 on 2022-06-27 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cineflix', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=models.TextField(max_length=200, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='poster',
            field=models.ImageField(upload_to='images/', verbose_name='foto'),
        ),
    ]