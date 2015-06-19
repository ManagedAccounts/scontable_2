from django.conf.urls import include, url
from home.views import index


urlpatterns = [
    url(r'^$', index , name = 'inicio'),
]
