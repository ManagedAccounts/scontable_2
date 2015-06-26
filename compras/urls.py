from django.conf.urls import include, url
from compras.views import OrdencompraList


urlpatterns = [
    url(r'^$', OrdencompraList.as_view(), name = 'compras_l'),
#    url(r'^search/$', clientesearch, name ='clientes_s'),
]
