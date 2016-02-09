from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^ajustar', views.reponer_gastar_producto, name='ajustar'),
    url(r'^buscar', views.buscar, name='buscar'),
    url(r'^nuevo$', views.nuevo_producto, name='nuevo'),
    url(r'^stockbajo$', views.stock_bajo, name='stockbajo'),
    url(r'^detalles/(?P<id>[0-9]+)$', views.detalles_producto, name='detalles'),
    url(r'^modificar/(?P<id>[0-9]+)$', views.modificar_producto, name='modificar'),
    url(r'^eliminar/(?P<id>[0-9]+)$', views.eliminar_producto, name='eliminar'),
    url(r'^$', views.index, name='index'),
]
