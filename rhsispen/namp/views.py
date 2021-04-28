# Create your views here.
from django.shortcuts import render, redirect
from .models import Setor, Equipe, Servidor, TipoJornada, Jornada
from django.http import HttpResponse, HttpResponseRedirect
from weasyprint import HTML
from django.template.loader import render_to_string
import tempfile
from django.core.files.storage import FileSystemStorage
import json
from .forms import DefinirJornadaRegularForm
from django.urls import resolve
from urllib.parse import urlparse
from datetime import timedelta as TimeDelta, datetime as DateTime, date as Date

'''
	Recuperar do banco as equipes da unidade penal escolhida no momento do cadastro de servidor e
	as envia para a página populando o campo select fk_equipe
'''
def get_equipes(request):
	result = list(Equipe.objects.none())
	id_setor = request.GET.get('id_setor', '')
	if (id_setor):
		result = list(Equipe.objects.filter(fk_setor=id_setor).values('id_equipe', 'nome'))
	return HttpResponse(json.dumps(result), content_type="application/json")

def get_tipo_jornada(request):
	result = list(TipoJornada.objects.none())
	id_equipe = request.GET.get('id_equipe', '')
	if (id_equipe):
		equipe = Equipe.objects.get(id_equipe=id_equipe)
		if equipe.categoria == 'Plantão':
			result = list(TipoJornada.objects.filter(carga_horaria__in=[24, 48]).values('carga_horaria', 'tipificacao'))
			print(result)
		elif equipe.categoria == 'Expediente':
			result = list(TipoJornada.objects.filter(carga_horaria__in=[6, 8]).values('carga_horaria', 'tipificacao'))
			print(result)
	return HttpResponse(json.dumps(result), content_type="application/json")

def get_equipe_servidor(request):
	result = list(Equipe.objects.none())
	id_matricula = request.GET.get('id_matricula', '')
	if (id_matricula):
		result = list(Equipe.objects.filter(fk_setor=Servidor.objects.get(id_matricula=id_matricula).fk_setor).values('id_equipe', 'nome'))
	return HttpResponse(json.dumps(result), content_type="application/json")

def exportar_pdf(request):
	# Model data
	servidores = Servidor.objects.all()
	# Rendered
	html_string = render_to_string('pdf_template.html', {'servidores': servidores})
	html = HTML(string=html_string)
	result = html.write_pdf(target='/tmp/servidores.pdf')

	fs = FileSystemStorage('/tmp')
	with fs.open('servidores.pdf') as pdf:
		response = HttpResponse(pdf, content_type='application/pdf')
		response['Content-Disposition'] = 'attachment; filename="servidores.pdf"'
		return response
	return response

def definirjornadaregular(request):
	id_setor = request.META.get("HTTP_REFERER").split('/')
	form = DefinirJornadaRegularForm()
	form.fields['setor'].initial = id_setor[6]
	form.fields['equipe'].choices = [('', '--Selecione--')] + list(Equipe.objects.filter(fk_setor=id_setor[6]).values_list('id_equipe', 'nome'))
	#form.fields['tipo_jornada'].choices = [('', '--Selecione--')] + list(TipoJornada.objects.all().values_list('carga_horaria', 'tipificacao'))
	
	contexto = {
		'definirjornadaregularForm': form,
	}
	return render(request, 'namp/setor/gerarjornadaregular.html', contexto)

def gerarescalaregular(request):
	if request.method == "POST":
		form = DefinirJornadaRegularForm(request.POST)
		if form.is_valid():
			#print(form.cleaned_data)
			
			#{'setor': '040.CMEPARG', 'data_inicial': datetime.date(2021, 4, 28), 'data_final': datetime.date(2021, 4, 30), 'equipe': '40', 'tipo_jornada': '8'}

			servidores = Servidor.objects.filter(fk_equipe=form.cleaned_data['equipe'])
			#print(servidores)
			for servidor in servidores:
				data_inicial = form.cleaned_data['data_inicial']
				data_final = form.cleaned_data['data_final']
				delta = TimeDelta(days=1)
				while data_inicial <= data_final:
					#print (data_inicial)
					#crias as intândcias de jornadas aqui para cada data do período
					jornada = Jornada(
						data_inicial, 
						1, 
						servidor, 
						Equipe.objects.filter(id_equipe=form.cleaned_data['equipe']), 
						TipoJornada.objects.filter(carga_horaria=form.cleaned_data['tipo_jornada'])
					)
					jornada.save()
					data_inicial += delta
			return HttpResponseRedirect('/admin/namp/setor/')
		else:
			print ("Erro no formulário!")
			return render(request, 'namp/setor/gerarjornadaregular.html', {'definirjornadaregularForm': form})