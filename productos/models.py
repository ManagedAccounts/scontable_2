from django.db import models

# Create your models here.

class Producto(models.Model):
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
    tunidad = models.CharField( max_length = 2, choices = u )#unidad de medida Sunat
    pcompra = models.DecimalField(max_digits = 5, decimal_places = 2)#precio compra
    pmarca = models.CharField(max_length = 50, null=True )#Marca del producto
    pventa = models.DecimalField(max_digits = 5, decimal_places = 2)#precio venta
    descripcion = models.TextField()#descripcion brevve del producto
    pimg = models.ImageField(upload_to = 'media' )#imagen de l producto

    def __str__(self):
        return self.nombre

