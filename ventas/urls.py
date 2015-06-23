from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^comprobante/', 'ventas.views.comprobante'),
    url(r'^comprar/', 'ventas.views.comprar'),
    url(r'^comprobante_edit/','ventas.views.comprobante_edit'),
    url(r'^clientes/', 'ventas.views.clientes'),
    url(r'^cliente_edit/','ventas.views.cliente_edit'),
    url(r'^cliente_add/','ventas.views.cliente_add'),
]
