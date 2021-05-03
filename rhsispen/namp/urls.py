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
	url('admin/namp/setor/040.CMEPARG/change/escala-regular/', views.definirjornadaregular, name='definirjornadaregular'),
	url('gerarescalaregular/', views.gerarescalaregular, name='gerarescalaregular'),
	url(r'^export/xls/$', views.exportar_jornadas_excel, name='exportar_jornadas_excel'),
	url('add_noturno_pdf/', views.add_noturno_pdf, name='add_noturno_pdf'),
	
]