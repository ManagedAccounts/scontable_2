"""scontable URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings


from accounts.views import ControlPanelView, LoginView, LogoutView, CreateUserView

urlpatterns = [
    url(r'^clientes/', include('clientes.urls', namespace = "clientes")),
    url(r'^compras/', include('compras.urls', namespace = "compras")),
    url(r'^factura/', include('ventas.urls', namespace = "ventas")),
    url(r'^productos/', include('productos.urls', namespace = "productos")),
    url(r'^proveedores/', include('proveedores.urls', namespace = "proveedores")),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}),


    url(r'^$', ControlPanelView.as_view(), name='inicio' ),
    url(r'^login/$',LoginView.as_view(), name='login'),
    url(r'^logout/$',LogoutView.as_view(), name='logout'),
    url(r'^signup/$',CreateUserView.as_view(), name='signup'),
    url(r'^factura/venta$', 'ventas.views.facturaCrear',
        name="factura_venta"),
    url(r'^factura/buscar_cliente$', 'ventas.views.buscarCliente'),
    url(r'^factura/buscar_producto$', 'ventas.views.buscarProducto'),

    url(r'^factura/consultar$', 'ventas.views.consultarFactura', name="consultar_factura"),

    #==================================================================
    url(r'^clientes/$','ventas.views.clientes'),
    url(r'^clienteAdd/$','ventas.views.clienteAdd'),
    url(r'^clienteEdit/(?P<id>\d+)$','ventas.views.clienteEdit'),
    url(r'^clienteDelete/(?P<id>\d+)$','ventas.views.clienteDelete'),
    url(r'^productos/$','ventas.views.productos'),
    url(r'^productoAdd/$','ventas.views.productoAdd'),
    url(r'^productoEdit/(?P<id>\d+)$','ventas.views.productoEdit'),
    url(r'^productoDelete/(?P<id>\d+)$','ventas.views.productoDelete'),
    url(r'^categoria/$','ventas.views.categoria'),
    url(r'^categoriaAdd/$','ventas.views.categoriaAdd'),
    url(r'^categoriaEdit/(?P<id>\d+)$','ventas.views.categoriaEdit'),
    url(r'^categoriaDelete/(?P<id>\d+)$','ventas.views.categoriaDelete'),

]


