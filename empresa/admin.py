from django.contrib import admin
from .models import Endereco

class EnderecoAdmin (admin.ModelAdmin):
    empty_value_display = "NA"

# Register your models here.
admin.site.register(Endereco, EnderecoAdmin)