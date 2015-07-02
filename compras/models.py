from django.db import models
from proveedores.models import Proveedor
from productos.models import Producto

# Create your models here.

class Ordencompra(models.Model):
    TIPO_PAGO = (
        ('e', 'Efectivo'),
        ('c', 'Credito')
    )

    TIPO_COMPROBANTE = (
        ('01', 'Factura'),
        ('03', 'Boleta de Venta'),
        ('07', 'Nota de Credito'),
        ('08', 'Nota de Debito'),
        ('60', 'Control Interno'),
    )

    tcomprobante = models.CharField(max_length = 2, choices = TIPO_COMPROBANTE)
    ccompra = models.PositiveIntegerField()
    aproucto = models.ManyToManyField(Producto)
    tpago = models.CharField(max_length = 1, choices = TIPO_PAGO)
    fecha = models.DateTimeField()

    def __str__(self):
        return self.aproucto.nombre


