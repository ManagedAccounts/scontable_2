from django.conf.urls import include, url
from productos.views import ProductoCreate, ProductoList

urlpatterns = [
    url(r'^add/$', ProductoCreate.as_view(), name = 'productos_c'),
    url(r'^$', ProductoList.as_view(), name = 'productos_l'),
]
