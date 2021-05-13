from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls import url

app_name = 'autenticacao'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
    	template_name='autenticacao/login.html'), 
    	name='login'),
    path('sair/', views.sair,name='logout'),
    path('cadastro/',views.cadastro,name='cadastro'),
]
