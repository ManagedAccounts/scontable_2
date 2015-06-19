from django.db import models
from proveedores.models import Proveedor
from productos.models import Producto

# Create your models here.

class Ordencompra(models.Model):
    TIPO_PAGO = (
        ('e', 'Efectivo'),
        ('c', 'Credito')
    )
    ocompra = models.PositiveIntegerField()
    pcompra = models.ForeignKey(Proveedor)
    aproucto = models.ForeignKey(Producto)
    tpago = models.CharField(max_length = 1, choices = TIPO_PAGO)
    fecha = models.DateTimeField()
    descripcion = models.TextField()
    cantidad = models.PositiveIntegerField()
    uprecio = models.DecimalField(max_digits = 5, decimal_places =2)

    def __str__(self):
        return self.aproucto.nombre


