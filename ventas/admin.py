from django.contrib import admin
from .models import Comprobante, Cliente, Detalle
"""
class ComprobanteAdmin(admin.ModelAdmin):
    list_display=['num_factura','num_boleta','fecha','igv','total']
    list_filter=['cliente']

class ClienteAdmin(admin.ModelAdmin):
    list_display=['ruc','razon_social','direccion']

class DetalleAdmin(admin.ModelAdmin):
    list_filter=['comprobante','articulo']
    list_display=['cantidad','importe']

admin.site.register(Comprobante, comprobanteAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Detalle, DetalleAdmin)

"""
admin.site.register(Comprobante)
admin.site.register(Cliente)
admin.site.register(Detalle)
