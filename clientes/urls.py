from django.conf.urls import include, url
from clientes.views import ClienteList, ClienteCreate, ClienteView

urlpatterns = [
    url(r'^$', ClienteList.as_view(), name = 'clientes_l'),
    url(r'^add/$', ClienteCreate.as_view(), name = 'clientes_c'),
    url(r'^search/$', ClienteView.as_view(), name ='clientes_s'),
]
