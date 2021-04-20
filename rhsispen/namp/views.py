# Create your views here.
from django.shortcuts import render
from .models import Setor, Equipe, Servidor
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

