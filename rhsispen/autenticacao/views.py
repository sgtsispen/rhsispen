from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from . forms import CadastroForm
from django.contrib import messages
from namp.models import Servidor
from django.contrib.auth.models import User

@login_required
def sair(request):
    logout(request)
    return redirect('/')	

def cadastro(request, template_name='autenticacao/cadastro.html'):
	if request.method == 'POST':
		form = CadastroForm(request.POST)
		if form.is_valid():
			try:
				servidor = Servidor.objects.get(id_matricula=form.cleaned_data.get('matricula'),cpf=form.cleaned_data.get('cpf'))
				if servidor:
					user = form.save(commit=False)
					if User.objects.filter(email=user.email).exists():
						messages.warning(request, 'O E-MAIL informado pertence aos registros de outro servidor.')
						return render(request, template_name,{'form': form})
					user.save()
					servidor.fk_user = user
					servidor.save()
			except Servidor.DoesNotExist:
				messages.warning(request, 'Servidor sem cadastro prévio! Verifique CPF, MATRÍCULA e E-MAIL informados ou acione o suporte.')
				return render(request, template_name,{'form': form})
		else:
			return render(request, template_name,{'form': form})	
		messages.info(request, 'Cadastro realizado com sucesso!')
		return redirect('/autenticacao/login/')
	else:
		form = CadastroForm()
		return render(request, template_name,{'form': form})