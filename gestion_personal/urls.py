from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^buscar', views.buscar, name='buscar'),
    url(r'^alta$', views.alta_personal, name='alta'),
    url(r'^detalles/(?P<id>[0-9]+)$', views.detalles_personal, name='detalles'),
    url(r'^modificar/(?P<id>[0-9]+)$', views.modificar_personal, name='modificar'),
    url(r'^eliminar/(?P<id>[0-9]+)$', views.eliminar_personal, name='eliminar'),
    url(r'^$', views.index, name='index'),
]
