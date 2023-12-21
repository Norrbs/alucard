# Generated by Django 4.2.8 on 2023-12-21 02:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aluguel', '0007_alter_cliente_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aluguel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inicial', models.DateField(verbose_name='Data Inicial')),
                ('data_final', models.DateField(blank=True, null=True, verbose_name='Data Final')),
                ('carro', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='carro', to='aluguel.carro', verbose_name='Carro')),
                ('cliente', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cliente', to='aluguel.cliente', verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Aluguel',
                'verbose_name_plural': 'Aluguéis',
            },
        ),
    ]