from django.contrib import admin
from .models import Tecnologias, Empresa, Vagas

# Register your models here.
@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
     list_display = ("nome", "email", "cidade", "nicho_mercado")
     list_editable = ("nicho_mercado",)
    



admin.site.register(Tecnologias)
admin.site.register(Vagas)
