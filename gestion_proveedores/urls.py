from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^buscar', views.buscar, name='buscar'),
    url(r'^alta$', views.altaProveedor, name='alta'),
    url(r'^detalles/(?P<id>[0-9]+)$', views.detallesProveedor, name='detalles'),
    url(r'^modificar/(?P<id>[0-9]+)$', views.modificarProveedor, name='modificar'),
    url(r'^eliminar/(?P<id>[0-9]+)$', views.eliminarProveedor, name='eliminar'),
    url(r'^$', views.index, name='index'),
]
