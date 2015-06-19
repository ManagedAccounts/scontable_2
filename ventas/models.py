#coding: utf-8
from django.db import models
from productos.models import Producto


class Cliente(models.Model):
    ruc=models.IntegerField()
    razon_social=models.CharField(max_length = 100)
    direccion=models.CharField(max_length = 100)
    def __unicode__(self):
        return self.razon_social

tabla_10=(
    ('00','otros'),
    ('01','Factura'),
    ('02','Recibo por honorarios'),
    ('03','Boleta'),
    ('04','Liquidacion de compra'),
    ('05','Boleto de compañia de aviacion comercial por el transporte aereo de pasajeros'),
    ('06','carta de porte aéreo'),
    ('07','Nota de crédito'),
    ('08','Nota de débito'),
    ('09','Guia de remisión'),
    ('10','Recibo por arrendamiento'),
    ('11','Póliza emitida por las bolsas de Valores, Bolsas de productos o agentes de intermediacion por operaciones realizadas en bolsas de valores o productos fuera de las mismas, autorizadas por CONASEV'),
    ('12','Ticket o cinta emitido por maquina registradora'),
    ('13','Documento emitido por bancos, instituciones financieras, crediticias y de seguros que se encuenten bajo el de la Superintendencia de Banca y Seguros'),
    ('14','Recibo por servicios públicos de suministro de energía eléctrica, agua, teléfono, telex y tlegráficos y otros, servicios complementarios que se incluyan en el recibo de servicio público'),
    ('15','Boleto emitido por las empresas de transporte público urbano de pasajeros'),
)

class Comprobante(models.Model):
    cliente=models.ForeignKey(Cliente)
    tabla_10=models.CharField(max_length=2, choices=tabla_10, default=01)
    num_factura=models.IntegerField()
    num_boleta=models.IntegerField()
    fecha=models.DateField()
    igv=models.FloatField(default=0.00)
    total=models.FloatField(default=0.00)
    def __unicode__(self):
        return self.num_factura

class Detalle(models.Model):
    comprobante=models.ForeignKey(Comprobante)
    cantidad=models.IntegerField()
    articulo=models.ForeignKey(Producto)
    importe=models.FloatField(default=0.00)
    def __unicode__(self):
        return self.Comprobante

