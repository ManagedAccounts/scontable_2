from django.conf.urls import include, url
from proveedores.views import ProveedorList, ProveedorCreate

urlpatterns = [
    url(r'^$', ProveedorList.as_view(), name = 'proveedor_l'),
    url(r'^add/$', ProveedorCreate.as_view(), name = 'proveedor_c'),
    url(r'^add/$', ProveedorCreate.as_view(), name = 'proveedor_c'),
]
