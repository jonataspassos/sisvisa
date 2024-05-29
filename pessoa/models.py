from django.db import models
from endereco.models import Endereco

# Create your models here.
    
class PessoaFisica(models.Model):
    class Meta:
        verbose_name = "Pessoa Física"
        verbose_name_plural = "Pessoas Físicas"
    cpf = models.CharField(max_length=20, verbose_name="CPF",null=False,blank=False)
    nome = models.CharField(max_length=100, verbose_name="Nome",null=False,blank=False)
    certificacao = models.CharField(max_length=50, verbose_name="Certificação", null=True,blank=True)

class PessoaJuridica(models.Model):
    class Meta:
        verbose_name = "Pessoa Jurídica"
        verbose_name_plural = "Pessoas Jurídicas"
    cnpj = models.CharField(max_length=30, verbose_name="CNPJ",null=False,blank=False)
    razao_social = models.CharField(max_length=100, verbose_name="Razão Social",null=False,blank=False)
    atividade = models.CharField(max_length=100, verbose_name="Atividade",null=False,blank=False)
    ie = models.CharField(max_length=30, verbose_name="IE",null=False,blank=False)#Inscrição Estadual
    proprietario = models.ManyToManyField(PessoaFisica, related_name="Proprietario")
    responsavel_tecnico = models.ManyToManyField(PessoaFisica, related_name="ResponsavelTecnico")# responsaveis tecnicos - certificacao https://docs.djangoproject.com/en/5.0/topics/db/models/#extra-fields-on-many-to-many-relationships
    endereco = models.OneToOneField(Endereco,on_delete=models.CASCADE)# endereco - registra no documento também
    
#pessoa
class Pessoa(models.Model):
    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"
    fisica = models.OneToOneField(PessoaFisica, on_delete=models.CASCADE)
    juridica = models.OneToOneField(PessoaJuridica, on_delete=models.CASCADE)


