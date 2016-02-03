from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^ajustar', views.reponerGastarProducto, name='ajustar'),
    url(r'^buscar', views.buscar, name='buscar'),
    url(r'^nuevo$', views.nuevoProducto, name='nuevo'),
    url(r'^stockbajo$', views.stockBajo, name='stockbajo'),
    url(r'^detalles/(?P<id>[0-9]+)$', views.detallesProducto, name='detalles'),
    url(r'^modificar/(?P<id>[0-9]+)$', views.modificarProducto, name='modificar'),
    url(r'^eliminar/(?P<id>[0-9]+)$', views.eliminarProducto, name='eliminar'),
    url(r'^$', views.index, name='index'),
]
