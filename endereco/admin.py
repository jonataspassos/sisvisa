from django.contrib import admin

# Register your models here.
from .models import Endereco, Endereco3

class EnderecoAdmin (admin.ModelAdmin):
    empty_value_display = "NA"
    
class Endereco2Admin (admin.ModelAdmin):
    empty_value_display = "NA"

# Register your models here.
admin.site.register(Endereco, EnderecoAdmin)
admin.site.register(Endereco3, Endereco2Admin)