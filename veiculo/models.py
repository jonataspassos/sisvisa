from django.db import models
from pessoa.models import Pessoa,PessoaFisica

# Create your models here.
class Veiculo(models.Model):
    class Meta:
        verbose_name = "Veículo"
        verbose_name_plural = "Veículos"
    #empresa
    pessoa = models.ForeignKey(Pessoa,related_name="Titular", on_delete=models.RESTRICT)
    #proprietarios (é pra ser um só)
    proprietario = models.ForeignKey(PessoaFisica, related_name="Proprietario_Veiculo", verbose_name="Proprietário do Veículo", on_delete=models.RESTRICT,null=True)
    responsavel_tecnico = models.ManyToManyField(PessoaFisica,null=True, related_name="Responsavel_Tecnico_Veiculo")# responsaveis tecnicos - certificacao https://docs.djangoproject.com/en/5.0/topics/db/models/#extra-fields-on-many-to-many-relationships
    marca = models.CharField(max_length=30, verbose_name="Marca",null=False,default='')
    modelo = models.CharField(max_length=30, verbose_name="Modelo",null=False,default='')
    ano = models.CharField(max_length=15, verbose_name="Ano",null=False,default='')
    chassi = models.CharField(max_length=30, verbose_name="Chassi",null=False,default='')
    crlv = models.CharField(max_length=30, verbose_name="Crlv",null=False,default='')
    renavam = models.CharField(max_length=30, verbose_name="Renavam",null=False,default='')
    placa = models.CharField(max_length=30, verbose_name="Placa",null=False,default='')
    atividade = models.CharField(max_length=100, verbose_name="Atividade",null=False,default='')