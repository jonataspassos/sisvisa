from django.db import models
from pessoa.models import Pessoa,PessoaFisica

# Create your models here.
class Veiculo(models.Model):
    class Meta:
        verbose_name = "Veículo"
        verbose_name_plural = "Veículos"
    #empresa
    pessoa = models.ForeignKey(Pessoa,on_delete=models.CASCADE)
    #proprietarios (é pra ser um só)
    proprietario = models.ManyToManyField(PessoaFisica, related_name="Proprietario_Veiculo")
    responsavel_tecnico = models.ManyToManyField(PessoaFisica, related_name="Responsavel_Tecnico_Veiculo")# responsaveis tecnicos - certificacao https://docs.djangoproject.com/en/5.0/topics/db/models/#extra-fields-on-many-to-many-relationships
    #marca
    #modelo
    #ano
    #chassi
    #crlv
    #renavam
    #responsavel - certificacao
    #placa
    #atividade