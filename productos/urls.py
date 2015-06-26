from django.conf.urls import include, url
from productos.views import ProductoCreate

urlpatterns = [
    url(r'^$', ProductoCreate.as_view(), name = 'productos_c'),
]
