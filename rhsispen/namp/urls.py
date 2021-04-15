# coding=utf-8
from django.conf.urls import  url
from namp.views import *
from . import views

app_name = 'namp'

urlpatterns = [
	url('getEquipes/$', views.get_equipes),
	url('exportar_pdf/', views.exportar_pdf, name='exportar_pdf'),
]