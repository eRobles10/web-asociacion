# Generated by Django 3.1.1 on 2021-01-14 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20210113_0713'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='active',
            field=models.BooleanField(blank=True, null=True, verbose_name='Activa'),
        ),
        migrations.AlterField(
            model_name='post',
            name='active',
            field=models.BooleanField(blank=True, null=True, verbose_name='Activo'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='Posts', verbose_name='Imagen'),
        ),
    ]