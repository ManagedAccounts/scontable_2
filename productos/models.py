from django.db import models
from proveedores.models import Proveedor

# Create your models here.


class Producto(models.Model):
    tp = (
        ('01', 'Mercaderia'),
        ('02', 'Producto Terminado'),
        ('03', 'Materias Primas y Auxiliares'),
        ('04', 'Envases y Envalajes'),
        ('05', 'Suministros Diversos'),
        ('06', 'Inmueble Maquinaria y Equipo'),
    )

    u = (
        ('01','KILOGRAMOS'),
        ('02','LIBRAS'),
        ('03','TONELADAS LARGAS'),
        ('04','TONELADAS METRICAS'),
        ('05','TONELADAS CORTAS'),
        ('06','GRAMOS'),
        ('07','UNIDADES'),
        ('08','LITROS'),
        ('09','GALONES'),
        ('10','BARRILES'),
        ('11','LATAS'),
        ('12','CAJAS'),
        ('13','MILLARES'),
        ('14','METROS CUBICOS'),
        ('15','METROS'),
        ('99','OTROS'),
    )
    nombre = models.CharField(max_length = 100)
    cproducto = models.CharField(max_length = 30)#codigo del producto
    tproducto = models.CharField(max_length = 2, choices = tp)
    tunidad = models.CharField( max_length = 2, choices = u )#unidad de medida Sunat
    pmarca = models.CharField(max_length = 50, null=True )#Marca del producto
    pcompra = models.DecimalField(max_digits = 20, decimal_places = 2)#precio compra
    pventa = models.DecimalField(max_digits = 20, decimal_places = 2)#precio venta
    descripcion = models.TextField()#descripcion brevve del producto
    pimg = models.ImageField(upload_to = 'media' )#imagen de l producto
    cantidad = models.PositiveIntegerField()
    pcompra = models.OneToOneField(Proveedor)
    uprecio = models.DecimalField(max_digits = 20 decimal_places =2)

    def __str__(self):
        return self.nombre

