from django.conf.urls import url

from . import views

urlpatterns = [
    # Clientes
    url(r'^buscar', views.buscar, name='buscar'),
    url(r'^alta$', views.alta_cliente, name='alta'),
    url(r'^detalles/(?P<id>[0-9]+)$', views.detalles_cliente, name='detalles'),
    url(r'^modificar/(?P<id>[0-9]+)$', views.modificar_cliente, name='modificar'),
    url(r'^eliminar/(?P<id>[0-9]+)$', views.eliminar_cliente, name='eliminar'),

    # Revisiones
    url(r'^info_opto/(?P<id>[0-9]+)$', views.ver_resvisiones, name='info_opto'),
    url(r'^eliminarevision/(?P<id_rev>[0-9]+)$', views.eliminar_revision, name='eliminar_rev'),
    url(r'^nuevarevision/(?P<id>[0-9]+)$', views.nueva_revision, name='nueva_rev'),
    url(r'^detallesrevision/(?P<id_rev>[0-9]+)$', views.detalles_revision, name='detalles_rev'),
    url(r'^modificarrevision/(?P<id_rev>[0-9]+)$', views.modificar_revision, name='modificar_rev'),

    url(r'^$', views.index, name='index'),
]
