# Generated by Django 3.1.1 on 2021-01-14 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='url',
            field=models.URLField(blank=True, null=True, verbose_name='Enlace'),
        ),
    ]
