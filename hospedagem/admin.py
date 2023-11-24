from django.contrib import admin

from .models import Quarto, Cliente, Hospedagem, Consumo

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Quarto)
admin.site.register(Hospedagem)
admin.site.register(Consumo)