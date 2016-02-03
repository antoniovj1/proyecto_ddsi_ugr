from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^login/?', views.login_view, name='login'),
    url(r'^logout/?$', views.log_out, name='logout'),
    url(r'^inicio/?$', views.index_view, name='index'),
    url(r'^$', views.index_view, name='index'),
]
