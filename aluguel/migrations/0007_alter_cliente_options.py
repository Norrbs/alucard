# Generated by Django 4.2.8 on 2023-12-21 01:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aluguel', '0006_cliente'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cliente',
            options={'verbose_name': 'Cliente', 'verbose_name_plural': 'Clientes'},
        ),
    ]
