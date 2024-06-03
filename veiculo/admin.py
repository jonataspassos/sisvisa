from django.contrib import admin

# Register your models here.
from .models import Veiculo

class VeiculoAdmin (admin.ModelAdmin):
    empty_value_display = "NA"

# Register your models here.
admin.site.register(Veiculo, VeiculoAdmin)