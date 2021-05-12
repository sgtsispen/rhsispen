# coding=utf-8

from namp.views import *
from . import views
from django.conf.urls import  url
from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView

app_name = 'namp'

urlpatterns = [
    #path('', TemplateView.as_view(
    	#template_name='namp/home.html'
    	#), name='home'),	
	#path("login/",auth_views.LoginView.as_view(
		#template_name="accounts/login.html"
		#),name="login"),
	#path('jornadas/', TemplateView.as_view(
		#template_name='namp/jornada/jornadas.html'
		#), name='jornadas'),
	path("logout/",auth_views.LogoutView.as_view(template_name="logout.html"),name="auth-logout"),
	url('getEquipes/$', views.get_equipes),
	url('getTipoJornada/', views.get_tipo_jornada),
	url('getEquipeServidor/$', views.get_equipe_servidor),
	url('exportar_pdf/', views.exportar_pdf, name='exportar_pdf'),
	url('escala-regular/', views.definirjornadaregular, name='definirjornadaregular'),
	url('gerarescalaregular/', views.gerarescalaregular, name='gerarescalaregular'),

	url(r'^frequencia-excel/xls/$', views.exportar_frequencia_excel, name='exportar_frequencia_excel'),
	url(r'^jornadas-excel/xls/$', views.exportar_jornadas_excel, name='exportar_jornadas_excel'),	
	url(r'^adicional-noturno/xls/$', views.exportar_noturno_excel, name='exportar_noturno_excel'),
	
	#url('add_noturno_pdf/', views.add_noturno_pdf, name='add_noturno_pdf'),
	
]