# Generated by Django 4.1 on 2024-06-03 02:56

from django.db import migrations, models
import endereco.models


class Migration(migrations.Migration):

    dependencies = [
        ('endereco', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Endereco2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('endereco', endereco.models.EnderecoField(max_length=195, verbose_name='Endereço')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
            ],
            options={
                'verbose_name': 'Endereço 2',
                'verbose_name_plural': 'Endereços 2',
            },
        ),
        migrations.AlterField(
            model_name='endereco',
            name='cep',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='CEP'),
        ),
    ]