# Create your views here.
from django.shortcuts import render
from .models import Setor, Equipe, Servidor, Jornada
from django.http import HttpResponse
from weasyprint import HTML
from django.template.loader import render_to_string
import tempfile
from django.core.files.storage import FileSystemStorage
import json

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
