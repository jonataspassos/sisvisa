from django.contrib import admin

# Register your models here.
from .models import Endereco

class EnderecoAdmin (admin.ModelAdmin):
    empty_value_display = "NA"

# Register your models here.
admin.site.register(Endereco, EnderecoAdmin)