from django.conf.urls import include, url
from compras.views import OrdencompraList, OrdencompraCreate


urlpatterns = [
    url(r'^$', OrdencompraList.as_view(), name = 'compras_l'),
    url(r'^add/$', OrdencompraCreate.as_view(), name ='compras_c'),
]
