# Generated by Django 4.1 on 2024-05-29 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logradouro', models.CharField(max_length=50, verbose_name='Logradouro')),
                ('numero', models.CharField(max_length=10, verbose_name='Número')),
                ('complemento', models.CharField(blank=True, max_length=30, null=True, verbose_name='Complemento')),
                ('bairro', models.CharField(max_length=30, verbose_name='Bairro')),
                ('cidade', models.CharField(max_length=30, verbose_name='Cidade')),
                ('estado', models.CharField(max_length=30, verbose_name='Estado')),
                ('cep', models.CharField(blank=True, max_length=30, null=True, verbose_name='CEP')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
            ],
            options={
                'verbose_name': 'Endereço',
                'verbose_name_plural': 'Endereços',
            },
        ),
    ]