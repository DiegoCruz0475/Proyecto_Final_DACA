from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_inmobiliaria, name='inicio_inmobiliaria'),

    # Rutas Propiedades
    path('propiedades/', views.ver_propiedades, name='ver_propiedades'),
    path('propiedades/agregar/', views.agregar_propiedad, name='agregar_propiedad'),
    path('propiedades/actualizar/<int:id_propiedad>/', views.actualizar_propiedad, name='actualizar_propiedad'),
    path('propiedades/borrar/<int:id_propiedad>/', views.borrar_propiedad, name='borrar_propiedad'),

    # Rutas Propietarios
    path('propietarios/', views.ver_propietarios, name='ver_propietarios'),
    path('propietarios/agregar/', views.agregar_propietario, name='agregar_propietario'),
    path('propietarios/actualizar/<int:id_propietario>/', views.actualizar_propietario, name='actualizar_propietario'),
    path('propietarios/borrar/<int:id_propietario>/', views.borrar_propietario, name='borrar_propietario'),

    # Rutas Clientes
    path('clientes/', views.ver_clientes, name='ver_clientes'),
    path('clientes/agregar/', views.agregar_cliente, name='agregar_cliente'),
    path('clientes/actualizar/<int:id_cliente>/', views.actualizar_cliente, name='actualizar_cliente'),
    path('clientes/borrar/<int:id_cliente>/', views.borrar_cliente, name='borrar_cliente'),

    # Rutas Agentes
    path('agentes/', views.ver_agentes, name='ver_agentes'),
    path('agentes/agregar/', views.agregar_agente, name='agregar_agente'),
    path('agentes/actualizar/<int:id_agente>/', views.actualizar_agente, name='actualizar_agente'),
    path('agentes/borrar/<int:id_agente>/', views.borrar_agente, name='borrar_agente'),

    # Rutas Visitas
    path('visitas/', views.ver_visitas, name='ver_visitas'),
    path('visitas/agregar/', views.agregar_visita, name='agregar_visita'),
    path('visitas/actualizar/<int:id_visita>/', views.actualizar_visita, name='actualizar_visita'),
    path('visitas/borrar/<int:id_visita>/', views.borrar_visita, name='borrar_visita'),

    # Rutas Contratos Venta
    path('contratos_venta/', views.ver_contratos_venta, name='ver_contratos_venta'),
    path('contratos_venta/agregar/', views.agregar_contrato_venta, name='agregar_contrato_venta'),
    path('contratos_venta/actualizar/<int:id_contrato_venta>/', views.actualizar_contrato_venta, name='actualizar_contrato_venta'),
    path('contratos_venta/borrar/<int:id_contrato_venta>/', views.borrar_contrato_venta, name='borrar_contrato_venta'),

    # Rutas Contratos Alquiler
    path('contratos_alquiler/', views.ver_contratos_alquiler, name='ver_contratos_alquiler'),
    path('contratos_alquiler/agregar/', views.agregar_contrato_alquiler, name='agregar_contrato_alquiler'),
    path('contratos_alquiler/actualizar/<int:id_contrato_alquiler>/', views.actualizar_contrato_alquiler, name='actualizar_contrato_alquiler'),
    path('contratos_alquiler/borrar/<int:id_contrato_alquiler>/', views.borrar_contrato_alquiler, name='borrar_contrato_alquiler'),
]