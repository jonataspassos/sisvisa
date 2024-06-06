from django.db import models
from .utils import Endereco as EnderecoClass
from .forms import EnderecoField

# https://anilkumarvalluru.medium.com/designing-and-implementing-custom-fields-in-django-creating-dynamic-data-models-b57f9f935467
#
#from django.utils.translation import gettext_lazy as _
        
class EnderecoField(models.Field):
    description = "Campo endereço completo"
    
    def __init__(self, *args, **kwargs):
        kwargs["max_length"] = 250
        super().__init__(*args, **kwargs)
    
    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        del kwargs["max_length"]
        return name, path, args, kwargs
    
    def from_db_value(self, value, expression, connection):
        if value is None:
            return value
        return EnderecoClass.parse(value)

    def to_python(self, value):
        if isinstance(value, self.Endereco):
            return value

        if value is None:
            return value

        return EnderecoClass.parse(value)    
    
    def get_db_prep_value(self, value, connection, prepared=False):
        if value is not None:
            return value.tostr()
        return None
    
    # def formfield(self, **kwargs):
    #     # This is a fairly standard way to set up some defaults
    #     # while letting the caller override them.
    #     defaults = {"form_class": EnderecoField}
    #     defaults.update(kwargs)
    #     return super().formfield(**defaults)

    def formfield(self, **kwargs):
        return super().formfield(form_class=EnderecoField,**kwargs)

    def get_internal_type(self):
        return "CharField"
    
    def value_to_string(self, obj):
        value = self.value_from_object(obj)
        return value.tostr()
    

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
    cep = models.CharField(max_length=15, verbose_name="CEP",null=True,blank=True)

    created_at = models.DateTimeField(auto_now_add=True,verbose_name="Criado em")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Atualizado em")

    def __str__(self):
        return self.logradouro[:30] + ' ... ' + self.numero +' ' + self.complemento + ', '+ self.bairro
    
class Endereco3(models.Model):
    class Meta:
        verbose_name = "Endereço 3"
        verbose_name_plural = "Endereços 3"
    endereco = EnderecoField(verbose_name="Endereço")
    
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="Criado em")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Atualizado em")

    def __str__(self):
        return str(self.endereco)