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
]


