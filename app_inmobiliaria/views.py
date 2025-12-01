from django.shortcuts import render, redirect, get_object_or_404
from .models import Propiedad, Propietario, Cliente, Agente, Visita, ContratoVenta, ContratoAlquiler

def inicio_inmobiliaria(request):
    return render(request, 'inicio.html')

# ==========================
# VISTAS PROPIETARIO
# ==========================
def agregar_propietario(request):
    if request.method == 'POST':
        Propietario.objects.create(
            nombre=request.POST.get('nombre'),
            apellido=request.POST.get('apellido'),
            telefono=request.POST.get('telefono'),
            email=request.POST.get('email'),
            direccion_propietario=request.POST.get('direccion_propietario'),
            dni=request.POST.get('dni')
        )
        return redirect('ver_propietarios')
    return render(request, 'propietario/agregar_propietario.html')

def ver_propietarios(request):
    return render(request, 'propietario/ver_propietarios.html', {'propietarios': Propietario.objects.all()})

def actualizar_propietario(request, id_propietario):
    obj = get_object_or_404(Propietario, pk=id_propietario)
    if request.method == 'POST':
        obj.nombre = request.POST.get('nombre')
        obj.apellido = request.POST.get('apellido')
        obj.telefono = request.POST.get('telefono')
        obj.email = request.POST.get('email')
        obj.direccion_propietario = request.POST.get('direccion_propietario')
        obj.dni = request.POST.get('dni')
        obj.save()
        return redirect('ver_propietarios')
    return render(request, 'propietario/actualizar_propietario.html', {'propietario': obj})

def borrar_propietario(request, id_propietario):
    obj = get_object_or_404(Propietario, pk=id_propietario)
    if request.method == 'POST':
        obj.delete()
        return redirect('ver_propietarios')
    return render(request, 'propietario/borrar_propietario.html', {'propietario': obj})

# ==========================
# VISTAS PROPIEDAD
# ==========================
def agregar_propiedad(request):
    if request.method == 'POST':
        Propiedad.objects.create(
            direccion=request.POST.get('direccion'),
            tipo_propiedad=request.POST.get('tipo_propiedad'),
            num_habitaciones=request.POST.get('num_habitaciones'),
            num_banos=request.POST.get('num_banos'),
            superficie_m2=request.POST.get('superficie_m2'),
            precio_venta=request.POST.get('precio_venta'),
            precio_alquiler=request.POST.get('precio_alquiler'),
            estado_propiedad=request.POST.get('estado_propiedad'),
            fecha_publicacion=request.POST.get('fecha_publicacion'),
            descripcion=request.POST.get('descripcion'),
            id_propietario=get_object_or_404(Propietario, pk=request.POST.get('id_propietario'))
        )
        return redirect('ver_propiedades')
    return render(request, 'propiedad/agregar_propiedad.html', {'propietarios': Propietario.objects.all()})

def ver_propiedades(request):
    return render(request, 'propiedad/ver_propiedades.html', {'propiedades': Propiedad.objects.all()})

def actualizar_propiedad(request, id_propiedad):
    obj = get_object_or_404(Propiedad, pk=id_propiedad)
    if request.method == 'POST':
        obj.direccion = request.POST.get('direccion')
        obj.tipo_propiedad = request.POST.get('tipo_propiedad')
        obj.num_habitaciones = request.POST.get('num_habitaciones')
        obj.num_banos = request.POST.get('num_banos')
        obj.superficie_m2 = request.POST.get('superficie_m2')
        obj.precio_venta = request.POST.get('precio_venta')
        obj.precio_alquiler = request.POST.get('precio_alquiler')
        obj.estado_propiedad = request.POST.get('estado_propiedad')
        obj.fecha_publicacion = request.POST.get('fecha_publicacion')
        obj.descripcion = request.POST.get('descripcion')
        obj.id_propietario = get_object_or_404(Propietario, pk=request.POST.get('id_propietario'))
        obj.save()
        return redirect('ver_propiedades')
    return render(request, 'propiedad/actualizar_propiedad.html', {'propiedad': obj, 'propietarios': Propietario.objects.all()})

def borrar_propiedad(request, id_propiedad):
    obj = get_object_or_404(Propiedad, pk=id_propiedad)
    if request.method == 'POST':
        obj.delete()
        return redirect('ver_propiedades')
    return render(request, 'propiedad/borrar_propiedad.html', {'propiedad': obj})

# ==========================
# VISTAS CLIENTE
# ==========================
def agregar_cliente(request):
    if request.method == 'POST':
        Cliente.objects.create(
            nombre=request.POST.get('nombre'),
            apellido=request.POST.get('apellido'),
            telefono=request.POST.get('telefono'),
            email=request.POST.get('email'),
            preferencias_propiedad=request.POST.get('preferencias_propiedad'),
            presupuesto_maximo=request.POST.get('presupuesto_maximo'),
            fecha_registro=request.POST.get('fecha_registro'),
            dni=request.POST.get('dni')
        )
        return redirect('ver_clientes')
    return render(request, 'cliente/agregar_cliente.html')

def ver_clientes(request):
    return render(request, 'cliente/ver_clientes.html', {'clientes': Cliente.objects.all()})

def actualizar_cliente(request, id_cliente):
    obj = get_object_or_404(Cliente, pk=id_cliente)
    if request.method == 'POST':
        obj.nombre = request.POST.get('nombre')
        obj.apellido = request.POST.get('apellido')
        obj.telefono = request.POST.get('telefono')
        obj.email = request.POST.get('email')
        obj.preferencias_propiedad = request.POST.get('preferencias_propiedad')
        obj.presupuesto_maximo = request.POST.get('presupuesto_maximo')
        obj.fecha_registro = request.POST.get('fecha_registro')
        obj.dni = request.POST.get('dni')
        obj.save()
        return redirect('ver_clientes')
    return render(request, 'cliente/actualizar_cliente.html', {'cliente': obj})

def borrar_cliente(request, id_cliente):
    obj = get_object_or_404(Cliente, pk=id_cliente)
    if request.method == 'POST':
        obj.delete()
        return redirect('ver_clientes')
    return render(request, 'cliente/borrar_cliente.html', {'cliente': obj})

# ==========================
# VISTAS AGENTE
# ==========================
def agregar_agente(request):
    if request.method == 'POST':
        Agente.objects.create(
            nombre=request.POST.get('nombre'),
            apellido=request.POST.get('apellido'),
            telefono=request.POST.get('telefono'),
            email=request.POST.get('email'),
            licencia_agente=request.POST.get('licencia_agente'),
            fecha_contratacion=request.POST.get('fecha_contratacion'),
            salario=request.POST.get('salario'),
            comision_porcentaje=request.POST.get('comision_porcentaje')
        )
        return redirect('ver_agentes')
    return render(request, 'agente/agregar_agente.html')

def ver_agentes(request):
    return render(request, 'agente/ver_agentes.html', {'agentes': Agente.objects.all()})

def actualizar_agente(request, id_agente):
    obj = get_object_or_404(Agente, pk=id_agente)
    if request.method == 'POST':
        obj.nombre = request.POST.get('nombre')
        obj.apellido = request.POST.get('apellido')
        obj.telefono = request.POST.get('telefono')
        obj.email = request.POST.get('email')
        obj.licencia_agente = request.POST.get('licencia_agente')
        obj.fecha_contratacion = request.POST.get('fecha_contratacion')
        obj.salario = request.POST.get('salario')
        obj.comision_porcentaje = request.POST.get('comision_porcentaje')
        obj.save()
        return redirect('ver_agentes')
    return render(request, 'agente/actualizar_agente.html', {'agente': obj})

def borrar_agente(request, id_agente):
    obj = get_object_or_404(Agente, pk=id_agente)
    if request.method == 'POST':
        obj.delete()
        return redirect('ver_agentes')
    return render(request, 'agente/borrar_agente.html', {'agente': obj})

# ==========================
# VISTAS VISITA
# ==========================
def agregar_visita(request):
    if request.method == 'POST':
        Visita.objects.create(
            id_propiedad=get_object_or_404(Propiedad, pk=request.POST.get('id_propiedad')),
            id_cliente=get_object_or_404(Cliente, pk=request.POST.get('id_cliente')),
            id_agente=get_object_or_404(Agente, pk=request.POST.get('id_agente')),
            fecha_visita=request.POST.get('fecha_visita'),
            hora_visita=request.POST.get('hora_visita'),
            comentarios_cliente=request.POST.get('comentarios_cliente'),
            calificacion_propiedad=request.POST.get('calificacion_propiedad')
        )
        return redirect('ver_visitas')
    context = {
        'propiedades': Propiedad.objects.all(),
        'clientes': Cliente.objects.all(),
        'agentes': Agente.objects.all()
    }
    return render(request, 'visita/agregar_visita.html', context)

def ver_visitas(request):
    return render(request, 'visita/ver_visitas.html', {'visitas': Visita.objects.all()})

def actualizar_visita(request, id_visita):
    obj = get_object_or_404(Visita, pk=id_visita)
    if request.method == 'POST':
        obj.id_propiedad = get_object_or_404(Propiedad, pk=request.POST.get('id_propiedad'))
        obj.id_cliente = get_object_or_404(Cliente, pk=request.POST.get('id_cliente'))
        obj.id_agente = get_object_or_404(Agente, pk=request.POST.get('id_agente'))
        obj.fecha_visita = request.POST.get('fecha_visita')
        obj.hora_visita = request.POST.get('hora_visita')
        obj.comentarios_cliente = request.POST.get('comentarios_cliente')
        obj.calificacion_propiedad = request.POST.get('calificacion_propiedad')
        obj.save()
        return redirect('ver_visitas')
    context = {
        'visita': obj,
        'propiedades': Propiedad.objects.all(),
        'clientes': Cliente.objects.all(),
        'agentes': Agente.objects.all()
    }
    return render(request, 'visita/actualizar_visita.html', context)

def borrar_visita(request, id_visita):
    obj = get_object_or_404(Visita, pk=id_visita)
    if request.method == 'POST':
        obj.delete()
        return redirect('ver_visitas')
    return render(request, 'visita/borrar_visita.html', {'visita': obj})

# ==========================
# VISTAS CONTRATO VENTA
# ==========================
def agregar_contrato_venta(request):
    if request.method == 'POST':
        ContratoVenta.objects.create(
            id_propiedad=get_object_or_404(Propiedad, pk=request.POST.get('id_propiedad')),
            id_propietario=get_object_or_404(Propietario, pk=request.POST.get('id_propietario')),
            id_cliente=get_object_or_404(Cliente, pk=request.POST.get('id_cliente')),
            id_agente=get_object_or_404(Agente, pk=request.POST.get('id_agente')),
            fecha_contrato=request.POST.get('fecha_contrato'),
            precio_final=request.POST.get('precio_final'),
            fecha_cierre=request.POST.get('fecha_cierre'),
            estado_contrato=request.POST.get('estado_contrato'),
            comision_agente=request.POST.get('comision_agente')
        )
        return redirect('ver_contratos_venta')
    context = {
        'propiedades': Propiedad.objects.all(),
        'propietarios': Propietario.objects.all(),
        'clientes': Cliente.objects.all(),
        'agentes': Agente.objects.all()
    }
    return render(request, 'contrato_venta/agregar_contrato_venta.html', context)

def ver_contratos_venta(request):
    return render(request, 'contrato_venta/ver_contratos_venta.html', {'contratos': ContratoVenta.objects.all()})

def actualizar_contrato_venta(request, id_contrato_venta):
    obj = get_object_or_404(ContratoVenta, pk=id_contrato_venta)
    if request.method == 'POST':
        obj.id_propiedad = get_object_or_404(Propiedad, pk=request.POST.get('id_propiedad'))
        obj.id_propietario = get_object_or_404(Propietario, pk=request.POST.get('id_propietario'))
        obj.id_cliente = get_object_or_404(Cliente, pk=request.POST.get('id_cliente'))
        obj.id_agente = get_object_or_404(Agente, pk=request.POST.get('id_agente'))
        obj.fecha_contrato = request.POST.get('fecha_contrato')
        obj.precio_final = request.POST.get('precio_final')
        obj.fecha_cierre = request.POST.get('fecha_cierre')
        obj.estado_contrato = request.POST.get('estado_contrato')
        obj.comision_agente = request.POST.get('comision_agente')
        obj.save()
        return redirect('ver_contratos_venta')
    context = {
        'contrato': obj,
        'propiedades': Propiedad.objects.all(),
        'propietarios': Propietario.objects.all(),
        'clientes': Cliente.objects.all(),
        'agentes': Agente.objects.all()
    }
    return render(request, 'contrato_venta/actualizar_contrato_venta.html', context)

def borrar_contrato_venta(request, id_contrato_venta):
    obj = get_object_or_404(ContratoVenta, pk=id_contrato_venta)
    if request.method == 'POST':
        obj.delete()
        return redirect('ver_contratos_venta')
    return render(request, 'contrato_venta/borrar_contrato_venta.html', {'contrato': obj})

# ==========================
# VISTAS CONTRATO ALQUILER
# ==========================
def agregar_contrato_alquiler(request):
    if request.method == 'POST':
        ContratoAlquiler.objects.create(
            id_propiedad=get_object_or_404(Propiedad, pk=request.POST.get('id_propiedad')),
            id_propietario=get_object_or_404(Propietario, pk=request.POST.get('id_propietario')),
            id_cliente=get_object_or_404(Cliente, pk=request.POST.get('id_cliente')),
            id_agente=get_object_or_404(Agente, pk=request.POST.get('id_agente')),
            fecha_inicio=request.POST.get('fecha_inicio'),
            fecha_fin=request.POST.get('fecha_fin'),
            monto_alquiler_mensual=request.POST.get('monto_alquiler_mensual'),
            estado_contrato=request.POST.get('estado_contrato'),
            deposito_garantia=request.POST.get('deposito_garantia')
        )
        return redirect('ver_contratos_alquiler')
    context = {
        'propiedades': Propiedad.objects.all(),
        'propietarios': Propietario.objects.all(),
        'clientes': Cliente.objects.all(),
        'agentes': Agente.objects.all()
    }
    return render(request, 'contrato_alquiler/agregar_contrato_alquiler.html', context)

def ver_contratos_alquiler(request):
    return render(request, 'contrato_alquiler/ver_contratos_alquiler.html', {'contratos': ContratoAlquiler.objects.all()})

def actualizar_contrato_alquiler(request, id_contrato_alquiler):
    obj = get_object_or_404(ContratoAlquiler, pk=id_contrato_alquiler)
    if request.method == 'POST':
        obj.id_propiedad = get_object_or_404(Propiedad, pk=request.POST.get('id_propiedad'))
        obj.id_propietario = get_object_or_404(Propietario, pk=request.POST.get('id_propietario'))
        obj.id_cliente = get_object_or_404(Cliente, pk=request.POST.get('id_cliente'))
        obj.id_agente = get_object_or_404(Agente, pk=request.POST.get('id_agente'))
        obj.fecha_inicio = request.POST.get('fecha_inicio')
        obj.fecha_fin = request.POST.get('fecha_fin')
        obj.monto_alquiler_mensual = request.POST.get('monto_alquiler_mensual')
        obj.estado_contrato = request.POST.get('estado_contrato')
        obj.deposito_garantia = request.POST.get('deposito_garantia')
        obj.save()
        return redirect('ver_contratos_alquiler')
    context = {
        'contrato': obj,
        'propiedades': Propiedad.objects.all(),
        'propietarios': Propietario.objects.all(),
        'clientes': Cliente.objects.all(),
        'agentes': Agente.objects.all()
    }
    return render(request, 'contrato_alquiler/actualizar_contrato_alquiler.html', context)

def borrar_contrato_alquiler(request, id_contrato_alquiler):
    obj = get_object_or_404(ContratoAlquiler, pk=id_contrato_alquiler)
    if request.method == 'POST':
        obj.delete()
        return redirect('ver_contratos_alquiler')
    return render(request, 'contrato_alquiler/borrar_contrato_alquiler.html', {'contrato': obj})