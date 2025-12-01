from django.db import models

# ==========================================
# MODELO: PROPIETARIO
# ==========================================
class Propietario(models.Model):
    id_propietario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    direccion_propietario = models.CharField(max_length=255)
    fecha_registro = models.DateField(auto_now_add=True)
    dni = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# ==========================================
# MODELO: PROPIEDAD
# ==========================================
class Propiedad(models.Model):
    id_propiedad = models.AutoField(primary_key=True)
    direccion = models.CharField(max_length=255)
    tipo_propiedad = models.CharField(max_length=50)
    num_habitaciones = models.IntegerField()
    num_banos = models.IntegerField()
    superficie_m2 = models.DecimalField(max_digits=10, decimal_places=2)
    precio_venta = models.DecimalField(max_digits=15, decimal_places=2)
    precio_alquiler = models.DecimalField(max_digits=15, decimal_places=2)
    estado_propiedad = models.CharField(max_length=50)
    fecha_publicacion = models.DateField()
    descripcion = models.TextField()
    id_propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE, related_name='propiedades')

    def __str__(self):
        return f"{self.tipo_propiedad} en {self.direccion}"

# ==========================================
# MODELO: CLIENTE
# ==========================================
class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    preferencias_propiedad = models.TextField()
    presupuesto_maximo = models.DecimalField(max_digits=15, decimal_places=2)
    fecha_registro = models.DateField()
    dni = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# ==========================================
# MODELO: AGENTE
# ==========================================
class Agente(models.Model):
    id_agente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    licencia_agente = models.CharField(max_length=50)
    fecha_contratacion = models.DateField()
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    comision_porcentaje = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# ==========================================
# OTROS MODELOS
# ==========================================
class Visita(models.Model):
    id_visita = models.AutoField(primary_key=True)
    id_propiedad = models.ForeignKey(Propiedad, on_delete=models.CASCADE)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    id_agente = models.ForeignKey(Agente, on_delete=models.CASCADE)
    fecha_visita = models.DateField()
    hora_visita = models.TimeField()
    comentarios_cliente = models.TextField()
    calificacion_propiedad = models.IntegerField()

class ContratoVenta(models.Model):
    id_contrato_venta = models.AutoField(primary_key=True)
    id_propiedad = models.ForeignKey(Propiedad, on_delete=models.CASCADE)
    id_propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    id_agente = models.ForeignKey(Agente, on_delete=models.CASCADE)
    fecha_contrato = models.DateField()
    precio_final = models.DecimalField(max_digits=15, decimal_places=2)
    fecha_cierre = models.DateField()
    estado_contrato = models.CharField(max_length=50)
    comision_agente = models.DecimalField(max_digits=10, decimal_places=2)

class ContratoAlquiler(models.Model):
    id_contrato_alquiler = models.AutoField(primary_key=True)
    id_propiedad = models.ForeignKey(Propiedad, on_delete=models.CASCADE)
    id_propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    id_agente = models.ForeignKey(Agente, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    monto_alquiler_mensual = models.DecimalField(max_digits=10, decimal_places=2)
    estado_contrato = models.CharField(max_length=50)
    deposito_garantia = models.DecimalField(max_digits=10, decimal_places=2)