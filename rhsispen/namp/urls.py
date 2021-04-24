# coding=utf-8
from django.conf.urls import  url
from namp.views import *
from . import views

app_name = 'namp'

urlpatterns = [
	url('getEquipes/$', views.get_equipes),
	url('getEquipeServidor/$', views.get_equipe_servidor),
	url('exportar_pdf/', views.exportar_pdf, name='exportar_pdf'),
	url('add_noturno_pdf/', views.add_noturno_pdf, name='add_noturno_pdf'),
]