# Generated by Django 4.1 on 2024-05-29 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('endereco', '0001_initial'),
        ('pessoa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Pessoa',
                'verbose_name_plural': 'Pessoas',
            },
        ),
        migrations.CreateModel(
            name='PessoaFisica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=20, verbose_name='CPF')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('certificacao', models.CharField(blank=True, max_length=50, null=True, verbose_name='Certificação')),
            ],
            options={
                'verbose_name': 'Pessoa Física',
                'verbose_name_plural': 'Pessoas Físicas',
            },
        ),
        migrations.CreateModel(
            name='PessoaJuridica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnpj', models.CharField(max_length=30, verbose_name='CNPJ')),
                ('razao_social', models.CharField(max_length=100, verbose_name='Razão Social')),
                ('atividade', models.CharField(max_length=100, verbose_name='Atividade')),
                ('ie', models.CharField(max_length=30, verbose_name='IE')),
                ('endereco', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='endereco.endereco')),
                ('proprietario', models.ManyToManyField(related_name='Proprietario', to='pessoa.pessoafisica')),
                ('responsavel_tecnico', models.ManyToManyField(related_name='ResponsavelTecnico', to='pessoa.pessoafisica')),
            ],
            options={
                'verbose_name': 'Pessoa Jurídica',
                'verbose_name_plural': 'Pessoas Jurídicas',
            },
        ),
        migrations.DeleteModel(
            name='Endereco',
        ),
        migrations.AddField(
            model_name='pessoa',
            name='fisica',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pessoa.pessoafisica'),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='juridica',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pessoa.pessoajuridica'),
        ),
    ]