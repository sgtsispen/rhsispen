# coding=utf-8
from django.conf.urls import  url
from namp.views import *
from . import views

app_name = 'namp'

urlpatterns = [
	url('getEquipes/$', views.get_equipes),
	url('getTipoJornada/', views.get_tipo_jornada),
	url('getEquipeServidor/$', views.get_equipe_servidor),
	url('exportar_pdf/', views.exportar_pdf, name='exportar_pdf'),
	url('definirjornadaregular/', views.definirjornadaregular, name='definirjornadaregular'),
	url('gerarescalaregular/', views.gerarescalaregular, name='gerarescalaregular'),
	
]