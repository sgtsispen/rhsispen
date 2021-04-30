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
from django.contrib import messages
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

'''def gerarescalaregular(request):
	if request.method == "POST":
		form = DefinirJornadaRegularForm(request.POST)
		if form.is_valid():
			servidores = Servidor.objects.filter(fk_equipe=form.cleaned_data['equipe'])
			for servidor in servidores:
				data_inicial = form.cleaned_data['data_inicial']
				data_final = form.cleaned_data['data_final']
				delta = TimeDelta(days=1)
				while data_inicial <= data_final:
					jornada = Jornada(data_jornada=data_inicial, assiduidade=1, fk_servidor=servidor, fk_equipe=Equipe.objects.get(id_equipe=form.cleaned_data['equipe']), fk_tipo_jornada=TipoJornada.objects.get(carga_horaria=form.cleaned_data['tipo_jornada']))
					jornada.save()
					data_inicial += delta
			return HttpResponseRedirect('/admin/namp/setor/')
		else:
			return render(request, 'namp/setor/gerarjornadaregular.html', {'definirjornadaregularForm': form})'''


def datasportipodejornada(data_inicial, data_final, tipo_jornada):
	datas = []
	if tipo_jornada == 6 or tipo_jornada == 8:
		intervalo = TimeDelta(days=1)
		while data_inicial <= data_final:
			if data_inicial.weekday() < 5: 
				datas.append(data_inicial)
			data_inicial+= intervalo
		return datas
	elif tipo_jornada == 24:
		intervalo = TimeDelta(days=4)
		while data_inicial <= data_final:
			datas.append(data_inicial)
			data_inicial+= intervalo
		return datas
	elif tipo_jornada == 48:
		intervalo = TimeDelta(days=8)
		while data_inicial <= data_final:
			datas.append(data_inicial)
			datas.append(Date.fromordinal(data_inicial.toordinal()+1))
			data_inicial+= intervalo
		return datas

def gerarescalaregular(request):
	if request.method == "POST":
		form = DefinirJornadaRegularForm(request.POST)
		if form.is_valid():
			equipe = Equipe.objects.get(id_equipe=form.cleaned_data['equipe'])
			servidores = Servidor.objects.filter(fk_equipe=form.cleaned_data['equipe'])
			for servidor in servidores:
				data_inicial = Date.fromordinal(min(form.cleaned_data['data_inicial'].toordinal(), form.cleaned_data['data_final'].toordinal()))
				data_final = Date.fromordinal(max(form.cleaned_data['data_inicial'].toordinal(), form.cleaned_data['data_final'].toordinal()))
				datas = datasportipodejornada(data_inicial, data_final, int(form.cleaned_data['tipo_jornada']))
				print(datas)
				for data in datas:
					jornada = Jornada(data_jornada=data, assiduidade=1, fk_servidor=servidor, fk_equipe=Equipe.objects.get(id_equipe=form.cleaned_data['equipe']), fk_tipo_jornada=TipoJornada.objects.get(carga_horaria=form.cleaned_data['tipo_jornada']))
					jornadas = Jornada.objects.filter(fk_servidor=jornada.fk_servidor).filter(data_jornada=jornada.data_jornada)
					if jornadas:
						continue
					jornada.save()
			messages.success(request, 'As jornadas da equipe ' + equipe.nome.upper() + ' foram atualizadas com suceso!')
			return HttpResponseRedirect('/admin/namp/setor/'+ form.cleaned_data['setor'] + '/change')
		else:
			messages.warning(request, 'Ops! Verifique os campos do formulário!')
			return render(request, 'namp/setor/gerarjornadaregular.html', {'definirjornadaregularForm': DefinirJornadaRegularForm(initial={'setor':form.cleaned_data['setor']})})
	else:
		return render(request, 'namp/setor/gerarjornadaregular.html', {'definirjornadaregularForm': DefinirJornadaRegularForm(initial={'setor':form.cleaned_data['setor']})})


def add_noturno_pdf(request):
	# Model data
	jornadas = Jornada.objects.all()
	# Rendered
	html_string = render_to_string('pdf_template2.html', {'jornadas': jornadas})
	html = HTML(string=html_string)
	result = html.write_pdf(target='/tmp/jornadas.pdf')
	
	fs = FileSystemStorage('/tmp')
	with fs.open('jornadas.pdf') as pdf:
		response = HttpResponse(pdf, content_type='application/pdf')
		response['Content-Disposition'] = 'attachment; filename="jornadas.pdf"'
		return response
	return response
"""
	# Model
	jornada = Jornada.objects.all()
	#Calculo
	inicioMes = DateTime.strptime(inicio, '%d' == 1)
	
	fimMes = inicioMes + TimeDelta(hours=obj.fk_tipo_jornada.carga_horaria)

	#Calculo 2 
	def calculo(d1, d2):
		d1 = datetime.timedelta(d1 = 2)#noite
		d2 = datetime.timedelta(d2 = 5)#dia
		return calc(d1.hours + d2.hours)
	#Calculo = quant de plantoes X 7 hrs
	return response
"""