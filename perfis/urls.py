from django.conf.urls import patterns, include, url
from django.contrib import admin
from perfis import views

urlpatterns = patterns('',
   
    url(r'^$', views.index, name='index'),
    url(r'^perfis/(?P<perfil_id>\d+)$',views.exibir, name='exibir'),
    url(r'^perfis/(?P<perfil_id>\d+)/convidar$',views.convidar, name='convidar'),
    url(r'^convites/(?P<convite_id>\d+)/aceitar', views.aceitar, name='aceitar'),
    url(r'^convites/(?P<contato_id>\d+)/remover_contato', views.remover_contato, name='remover_contato'),
    url(r'^convites/(?P<convite_id>\d+)/regeitar', views.regeitar, name='regeitar'),
)