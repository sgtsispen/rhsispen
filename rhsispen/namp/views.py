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
	id_setor = request.GET.get('id_setor', '')
	result = list(Equipe.objects.filter(fk_setor=id_setor).values('id_equipe', 'nome'))
	return HttpResponse(json.dumps(result), content_type="application/json")

def exportar_pdf(request):
	# Model data
	servidor = Servidor.objects.get(nome="Leonardo Araujo")
	# Rendered
	html_string = render_to_string('pdf_template.html', {'obj': servidor})
	html = HTML(string=html_string)
	result = html.write_pdf(target='/tmp/{}.pdf'.format(servidor))
	
	'''# Create http response
				response = HttpResponse(content_type='application/pdf;')
				response['Content-Disposition'] = 'inline; filename=pdf_template.html'
				response['Content-Transfer-Encoding'] = 'binary'
				with tempfile.NamedTemporaryFile(delete=True) as output:
					output.write(result)
					output.flush()
					output.open(output.name, 'r')
					response.write(output.read())
				return response'''

	fs = FileSystemStorage('/tmp')
	with fs.open('{}.pdf'.format(servidor)) as pdf:
		response = HttpResponse(pdf, content_type='application/pdf')
		response['Content-Disposition'] = 'attachment; filename="{}.pdf"'.format(servidor)
		return response
	return response