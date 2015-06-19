from django.conf.urls import include, url
from clientes.views import ClienteList

urlpatterns = [
    url(r'^$', ClienteList.as_view(), name = 'clientes_l'),
#    url(r'^search/$', clientesearch, name ='clientes_s'),
]
