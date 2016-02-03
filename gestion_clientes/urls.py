from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^buscar', views.buscar, name='buscar'),
    url(r'^alta$', views.altaCliente, name='alta'),
    url(r'^detalles/(?P<id>[0-9]+)$', views.detallesCliente, name='detalles'),
    url(r'^modificar/(?P<id>[0-9]+)$', views.modificarCliente, name='modificar'),
    url(r'^eliminar/(?P<id>[0-9]+)$', views.eliminarCliente, name='eliminar'),
    url(r'^$', views.index, name='index'),
]
