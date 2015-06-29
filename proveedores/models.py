from django.db import models

# Create your models here.

class Proveedor(models.Model):
    ESTADO = (
        (0, 'Activo'),
        (1, 'Inactivo'),
    )
    rsocial = models.CharField(max_length = 101)#Razon Social
    rod = models.PositiveSmallIntegerField() # RUC
    direccion = models.CharField(max_length = 100) #direccion
    toc = models.PositiveSmallIntegerField() # telefono o celular
    email = models.EmailField()
    contacto = models.CharField(max_length = 100) #Nombre del contacto
    descripcion = models.TextField()#Descripcion del proveedor

    def __str__(self):
        return self.rsocial


