# Generated by Django 3.1.1 on 2021-01-15 08:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_auto_20210115_0802'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='services',
            options={'ordering': ['order'], 'verbose_name': 'Servicios', 'verbose_name_plural': 'Servicios'},
        ),
        migrations.RenameField(
            model_name='services',
            old_name='orderPriority',
            new_name='order',
        ),
    ]
