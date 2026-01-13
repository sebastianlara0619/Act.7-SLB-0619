from django.db import models

class Cliente_CRM(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    empresa = models.CharField(max_length=255)
    email = models.EmailField(max_length=100)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=255)
    fecha_registro = models.DateTimeField()
    industria = models.CharField(max_length=100)
    sector = models.CharField(max_length=100)
    estado_cliente = models.CharField(max_length=50)
    fuente_lead = models.CharField(max_length=50)
    notas_cliente = models.TextField()

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.empresa})"

class Contacto_CRM(models.Model):
    id_contacto = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente_CRM, on_delete=models.CASCADE)
    nombre_contacto = models.CharField(max_length=100)
    apellido_contacto = models.CharField(max_length=100)
    email_contacto = models.EmailField(max_length=100)
    telefono_contacto = models.CharField(max_length=20)
    cargo_contacto = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    rol = models.CharField(max_length=50)

class Empleado_Comercial(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    telefono = models.CharField(max_length=20)
    cargo_comercial = models.CharField(max_length=100)
    fecha_contratacion = models.DateField()
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    cuota_ventas = models.DecimalField(max_digits=10, decimal_places=2)

class Oportunidad_Venta(models.Model):
    id_oportunidad = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente_CRM, on_delete=models.CASCADE)
    nombre_oportunidad = models.CharField(max_length=255)
    descripcion = models.TextField()
    valor_estimado = models.DecimalField(max_digits=15, decimal_places=2)
    etapa_venta = models.CharField(max_length=50)
    fecha_cierre_estimada = models.DateField()
    comercial_responsable = models.ForeignKey(Empleado_Comercial, on_delete=models.CASCADE)
    probabilidad_cierre = models.DecimalField(max_digits=3, decimal_places=2)
    fecha_creacion = models.DateTimeField()

class Actividad_CRM(models.Model):
    id_actividad = models.AutoField(primary_key=True)
    oportunidad = models.ForeignKey(Oportunidad_Venta, on_delete=models.CASCADE)
    contacto = models.ForeignKey(Contacto_CRM, on_delete=models.CASCADE)
    tipo_actividad = models.CharField(max_length=50)
    fecha_actividad = models.DateField()
    hora_actividad = models.TimeField()
    descripcion_actividad = models.TextField()
    estado_actividad = models.CharField(max_length=50)
    empleado_realizo = models.ForeignKey(Empleado_Comercial, on_delete=models.CASCADE)

class Producto_Servicio_CRM(models.Model):
    id_item = models.AutoField(primary_key=True)
    nombre_item = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio_lista = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_item = models.CharField(max_length=50)
    es_recurrente = models.BooleanField(default=False)
    fecha_lanzamiento = models.DateField()
    categoria_item = models.CharField(max_length=100)

class Detalle_Oportunidad(models.Model):
    id_detalle = models.AutoField(primary_key=True)
    oportunidad = models.ForeignKey(Oportunidad_Venta, on_delete=models.CASCADE)
    item = models.ForeignKey(Producto_Servicio_CRM, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_unitario_acordado = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal_item = models.DecimalField(max_digits=10, decimal_places=2)
    descuento_aplicado = models.DecimalField(max_digits=5, decimal_places=2)
    fecha_agregado = models.DateTimeField()