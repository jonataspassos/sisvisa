# https://django-polymorphic.readthedocs.io/en/stable/quickstart.html

from django.db import models
from endereco.models import Endereco
from polymorphic.models import PolymorphicModel
# pip install django-polymorphic

# Create your models here.
#pessoa
class Pessoa(PolymorphicModel):
    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"
    
class PessoaFisica(Pessoa):
    class Meta:
        verbose_name = "Pessoa Física"
        verbose_name_plural = "Pessoas Físicas"
    cpf = models.CharField(max_length=20, verbose_name="CPF",null=True, unique=True)
    nome = models.CharField(max_length=100, verbose_name="Nome",null=True)
    certificacao = models.CharField(max_length=50, verbose_name="Certificação", null=True,blank=True)

class PessoaJuridica(Pessoa):
    class Meta:
        verbose_name = "Pessoa Jurídica"
        verbose_name_plural = "Pessoas Jurídicas"
    cnpj = models.CharField(max_length=30, verbose_name="CNPJ",null=False,blank=False, unique=True)
    razao_social = models.CharField(max_length=100, verbose_name="Razão Social",null=False,blank=False)
    atividade = models.CharField(max_length=100, verbose_name="Atividade",null=False,blank=False)
    ie = models.CharField(max_length=30, verbose_name="IE",null=False,blank=False)#Inscrição Estadual
    proprietario = models.ManyToManyField(PessoaFisica, related_name="Proprietario")
    responsavel_tecnico = models.ManyToManyField(PessoaFisica, related_name="ResponsavelTecnico")# responsaveis tecnicos - certificacao https://docs.djangoproject.com/en/5.0/topics/db/models/#extra-fields-on-many-to-many-relationships
    endereco = models.OneToOneField(Endereco,on_delete=models.CASCADE)# endereco - registra no documento também
    



