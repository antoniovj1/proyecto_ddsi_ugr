from django.conf.urls import url

from . import views

urlpatterns = [
    #Clientes
    url(r'^buscar', views.buscar, name='buscar'),
    url(r'^alta$', views.altaCliente, name='alta'),
    url(r'^detalles/(?P<id>[0-9]+)$', views.detallesCliente, name='detalles'),
    url(r'^modificar/(?P<id>[0-9]+)$', views.modificarCliente, name='modificar'),
    url(r'^eliminar/(?P<id>[0-9]+)$', views.eliminarCliente, name='eliminar'),

    #Revisiones
    url(r'^info_opto/(?P<id>[0-9]+)$', views.verResvisiones, name='info_opto'),
    url(r'^eliminarevision/(?P<id_rev>[0-9]+)$', views.eliminarRevision, name='eliminar_rev'),
    url(r'^nuevarevision/(?P<id>[0-9]+)$', views.nuevaRevision, name='nueva_rev'),
    url(r'^detallesrevision/(?P<id_rev>[0-9]+)$', views.detallesRevision, name='detalles_rev'),
    url(r'^modificarrevision/(?P<id_rev>[0-9]+)$', views.modificarRevision, name='modificar_rev'),

    url(r'^$', views.index, name='index'),
]
