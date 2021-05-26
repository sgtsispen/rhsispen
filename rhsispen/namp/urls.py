# coding=utf-8

from namp.views import *
from . import views
from django.conf.urls import  url
from django.urls import path
from django.contrib.auth import views as auth_views

app_name = 'namp'

urlpatterns = [
	path('', views.home, name='home'),
	path('jornadas/', views.jornadas_operador, name='jornadas_operador'),
	url('getEquipes/$', views.get_equipes),
	url('getTipoJornada/', views.get_tipo_jornada),
	url('getEquipeServidor/$', views.get_equipe_servidor),
	url('escala-regular/', views.definirjornadaregular, name='definirjornadaregular'),
	url('gerarescalaregular/', views.gerarescalaregular, name='gerarescalaregular'),

	url('exportar_pdf/', views.exportar_pdf, name='exportar_pdf'),

	url(r'^frequencia-excel/xls/$', views.exportar_frequencia_excel, name='exportar_frequencia_excel'),
	url(r'^jornadas-excel/xls/$', views.exportar_jornadas_excel, name='exportar_jornadas_excel'),
	url(r'^adicional-noturno/xls/$', views.exportar_noturno_excel, name='exportar_noturno_excel'),
	
	
]