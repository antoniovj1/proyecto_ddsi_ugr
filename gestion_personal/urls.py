from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^buscar', views.buscar, name='buscar'),
    url(r'^alta$', views.altaPersonal, name='alta'),
    url(r'^detalles/(?P<id>[0-9]+)$', views.detallesPersonal, name='detalles'),
    url(r'^modificar/(?P<id>[0-9]+)$', views.modificarPersonal, name='modificar'),
    url(r'^eliminar/(?P<id>[0-9]+)$', views.eliminarPersonal, name='eliminar'),
    url(r'^$', views.index, name='index'),
]
