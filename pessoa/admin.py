# https://django-polymorphic.readthedocs.io/en/stable/admin.html

# https://medium.com/@SiddyZen/create-embedded-models-using-django-admin-3ecc38a00879

from django.contrib import admin
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin, PolymorphicChildModelFilter
# from .models import ModelA, ModelB, ModelC, StandardModel
from .models import Pessoa, PessoaJuridica, PessoaFisica


class PessoaChildAdmin(PolymorphicChildModelAdmin):
    """ Base admin class for all child models """
    base_model = Pessoa  # Optional, explicitly set here.

    # By using these `base_...` attributes instead of the regular ModelAdmin `form` and `fieldsets`,
    # the additional fields of the child models are automatically added to the admin form.
    # base_form = ...
    base_fieldsets = []


@admin.register(PessoaJuridica)
class PessoaJuridicaAdmin(PessoaChildAdmin):
    base_model = PessoaJuridica  # Explicitly set here!
    # define custom features here
#     base_fieldsets = [
#         (None,{'fields':['cnpj','razao_social']}),
#         ("Dados Específicos",{'fields':['atividade','ie']}),
#         ("Proprietários/Responsáveis",{'fields':['proprietario','responsavel_tecnico']}),
#         ("Endereço",{'fields':['endereco']})
#     ]


@admin.register(PessoaFisica)
class PessoaFisicaAdmin(PessoaChildAdmin):
    base_model = PessoaFisica  # Explicitly set here!
    show_in_index = True  # makes child model admin visible in main admin site
    # define custom features here
#     base_fieldsets = [
#         (None,{'fields':['cpf','nome']}),
#         ("Opcional",{'fields':['certificacao']})
#     ]    


@admin.register(Pessoa)
class ModelAParentAdmin(PolymorphicParentModelAdmin):
    """ The parent model admin """
    base_model = Pessoa  # Optional, explicitly set here.
    child_models = (PessoaJuridica, PessoaFisica)
    list_filter = (PolymorphicChildModelFilter,)  # This is optional.