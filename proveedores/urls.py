from django.conf.urls import include, url
from proveedores.views import ProveedorList

urlpatterns = [
    url(r'^$', ProveedorList.as_view(), name = 'proveedor_l'),
]
