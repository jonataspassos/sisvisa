from django.contrib import admin

# Register your models here.
from .models import Endereco

class EnderecoAdmin (admin.ModelAdmin):
    empty_value_display = "NA"
    fields=[
        'logradouro','numero','complemento','bairro','cidade','estado','cep'    ]
    list_display = ['cep','numero','complemento','endereco_str']#,'endereco'
    @admin.display(empty_value="---",description='Endereco')
    def endereco_str(self, obj):
        return str(obj)


# Register your models here.
admin.site.register(Endereco, EnderecoAdmin)