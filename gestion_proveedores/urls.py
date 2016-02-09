from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^buscar', views.buscar, name='buscar'),
    url(r'^alta$', views.alta_proveedor, name='alta'),
    url(r'^detalles/(?P<id>[0-9]+)$', views.detalles_proveedor, name='detalles'),
    url(r'^modificar/(?P<id>[0-9]+)$', views.modificar_proveedor, name='modificar'),
    url(r'^eliminar/(?P<id>[0-9]+)$', views.eliminar_proveedor, name='eliminar'),
    url(r'^$', views.index, name='index'),
]
