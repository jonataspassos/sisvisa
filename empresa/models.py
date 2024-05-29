from django.db import models

# Create your models here.
class Endereco(models.Model):
    class Meta:
        verbose_name = "Endereço"
        verbose_name_plural = "Endereços"
    logradouro = models.CharField(max_length=50, verbose_name="Logradouro",null=False,blank=False)
    numero = models.CharField(max_length=10, verbose_name="Número",null=False,blank=False)
    complemento = models.CharField(max_length=30, verbose_name="Complemento",null=True,blank=True)
    bairro = models.CharField(max_length=30, verbose_name="Bairro",null=False,blank=False)
    cidade = models.CharField(max_length=30, verbose_name="Cidade",null=False,blank=False)
    estado = models.CharField(max_length=30, verbose_name="Estado",null=False,blank=False)
    cep = models.CharField(max_length=30, verbose_name="CEP",null=True,blank=True)

    created_at = models.DateTimeField(auto_now_add=True,verbose_name="Criado em")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Atualizado em")

    def __str__(self):
        return self.logradouro[:30] + ' ... ' + self.numero +' ' + self.complemento + ', '+ self.bairro
    
#pessoa
    
class Empresa(models.Model):
    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"
    #cnpj
    #razao_social
    #atividade
    # inscrição-estadual (IE)
    # proprietarios - pessoa
    # responsaveis tecnicos - certificacao https://docs.djangoproject.com/en/5.0/topics/db/models/#extra-fields-on-many-to-many-relationships
    # endereco - registra no documento também

class Veiculo(models.Model):
    class Meta:
        verbose_name = "Veículo"
        verbose_name_plural = "Veículos"
    #empresa
    #marca
    #modelo
    #ano
    #chassi
    #crlv
    #renavam
    #proprietarios (é pra ser um só)
    #responsavel - certificacao
    #placa
    #atividade


