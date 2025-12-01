from django.contrib import admin
from .models import Propietario, Propiedad, Cliente, Agente, Visita, ContratoVenta, ContratoAlquiler

admin.site.register(Propietario)
admin.site.register(Propiedad)
admin.site.register(Cliente)
admin.site.register(Agente)
admin.site.register(Visita)
admin.site.register(ContratoVenta)
admin.site.register(ContratoAlquiler)