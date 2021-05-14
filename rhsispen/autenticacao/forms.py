from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CadastroForm(UserCreationForm):
	cpf = forms.CharField(max_length=11, help_text='Informe o seu CPF')
	matricula = forms.CharField(max_length=30, help_text='Matrícula sem o dígito do vínculo. Ex: 12345')

	class Meta:
		model = User
		fields = ('username', 'cpf', 'matricula', 'email', 'password1', 'password2', )