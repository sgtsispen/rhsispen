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
	url('escala-regular/', views.definirjornadaregular, name='definirjornadaregular'),
	url('gerarescalaregular/', views.gerarescalaregular, name='gerarescalaregular'),

	url(r'^jornadas-excel/xls/$', views.exportar_jornadas_excel, name='exportar_jornadas_excel'),
	
	url(r'^adicional-noturno/xls/$', views.exportar_noturno_excel, name='exportar_noturno_excel'),
	
	#url('add_noturno_pdf/', views.add_noturno_pdf, name='add_noturno_pdf'),
	
]