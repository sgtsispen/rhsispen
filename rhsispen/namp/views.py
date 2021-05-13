# Create your views here.
import tempfile
import json
import xlwt
from django.shortcuts import render, redirect
from .models import Setor, Equipe, Servidor, TipoJornada, Jornada
from django.http import HttpResponse, HttpResponseRedirect
from weasyprint import HTML
from django.template.loader import render_to_string
from django.core.files.storage import FileSystemStorage
from .forms import DefinirJornadaRegularForm
from django.urls import resolve
from urllib.parse import urlparse
from datetime import timedelta as TimeDelta, datetime as DateTime, date as Date
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='/autenticacao/login/')
def home(request,template_name='home.html'):
    return render(request,template_name, {})

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
	
	contexto = {
		'definirjornadaregularForm': form,
	}
	return render(request, 'namp/setor/gerarjornadaregular.html', contexto)

# métodos que retorna os dias do intervalo a partir do tipo de jornada
def datasportipodejornada(data_inicial, data_final, tipo_jornada):
	datas = []
	feriados = {
		"anonovo": Date(2021,1,1),
		"tiradentes": Date(2021,4,21),
		"trabalho": Date(2021,5,1),
		"independencia": Date(2021,9,7),
		"nsraparecida": Date(2021,10,12),
		"finados": Date(2021,11,2),
		"republica": Date(2021,11,15),
		"natal": Date(2021,12,25),
	}

	if tipo_jornada == 6 or tipo_jornada == 8:
		intervalo = TimeDelta(days=1)
		while data_inicial <= data_final:
			if data_inicial.weekday() not in (5,6) and data_inicial not in feriados.values():
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
				for data in datas:
					jornada = Jornada(data_jornada=data, assiduidade=1, fk_servidor=servidor, fk_equipe=Equipe.objects.get(id_equipe=form.cleaned_data['equipe']), fk_tipo_jornada=TipoJornada.objects.get(carga_horaria=form.cleaned_data['tipo_jornada']))
					jornadas = Jornada.objects.filter(fk_servidor=jornada.fk_servidor).filter(data_jornada=jornada.data_jornada)
					if jornadas:
						continue
					jornada.save()
			messages.success(request, 'As jornadas da equipe ' + equipe.nome.upper() + ' foram atualizadas com suceso!')
			return HttpResponseRedirect('/admin/namp/setor/'+ form.cleaned_data['setor'] + '/change/')
		else:
			messages.warning(request, 'Ops! Verifique os campos do formulário!')
			return render(request, 'namp/setor/gerarjornadaregular.html', {'definirjornadaregularForm': DefinirJornadaRegularForm(initial={'setor':form.cleaned_data['setor']})})
	else:
		return render(request, 'namp/setor/gerarjornadaregular.html', {'definirjornadaregularForm': DefinirJornadaRegularForm(initial={'setor':form.cleaned_data['setor']})})


def exportar_jornadas_excel(request):
	#recuperando as jornadas do banco. OBS: apenas as jornadas do mês corrente
	jornadas = Jornada.objects.filter(assiduidade=True).filter(data_jornada__month=Date.today().month).order_by('fk_equipe__fk_setor__nome', 'fk_equipe__nome','fk_servidor__nome','data_jornada')
	if jornadas:
		response = HttpResponse(content_type='application/ms-excel')
		response['Content-Disposition'] = 'attachment; filename="jornadas.xls"'

		wb = xlwt.Workbook(encoding='utf-8')
		ws = wb.add_sheet('Jornadas')

		# largura das colunas
		ws.col(0).width = 256 * 12
		ws.col(1).width = 256 * 9
		ws.col(2).width = 256 * 50
		ws.col(3).width = 256 * 12
		ws.col(4).width = 256 * 15
		ws.col(5).width = 256 * 18
		ws.col(6).width = 256 * 18
		ws.col(7).width = 256 * 18
		
		#cabeçalho, primeira linha
		row_num = 0

		font_style = xlwt.XFStyle()
		font_style.font.bold = True

		columns = ['MATRICULA', 'VINCULO', 'SERVIDOR', 'CPF', 'CODIGO', 'CARGA_HORARIA', 'INICIO', 'FIM' ]

		for col_num in range(len(columns)):
			ws.write(row_num, col_num, columns[col_num], font_style)

		# Sheet body, remaining rows
		font_style = xlwt.XFStyle()

		#aplicando os atributos das jornadas nas células da planilha
		for jornada in jornadas:
			row_num += 1   
			ws.write(row_num, 0, jornada.fk_servidor.id_matricula, font_style)
			ws.write(row_num, 1, jornada.fk_servidor.vinculo, font_style)
			ws.write(row_num, 2, jornada.fk_servidor.nome, font_style)
			ws.write(row_num, 3, jornada.fk_servidor.cpf, font_style)
			ws.write(row_num, 4, jornada.fk_equipe.fk_setor.id_setor, font_style)
			ws.write(row_num, 5, jornada.fk_tipo_jornada.carga_horaria, font_style)
			
			inicio = jornada.data_jornada.strftime("%d/%m/%Y") + " " +jornada.fk_equipe.hora_inicial.strftime("%H:%M:%S")
			ws.write(row_num, 6, DateTime.strptime(inicio, '%d/%m/%Y %H:%M:%S').strftime("%d/%m/%Y %H:%M:%S"), font_style)
			fim = DateTime.strptime(inicio, '%d/%m/%Y %H:%M:%S') + TimeDelta(hours=jornada.fk_tipo_jornada.carga_horaria)
			ws.write(row_num, 7, fim.strftime('%d/%m/%Y %H:%M:%S'), font_style)
		wb.save(response)
		return response
	messages.warning(request, 'Ops! Não há jornadas registradas no mês corrente!')
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

#def add_noturno_pdf(request):
#	jornadas = Jornada.objects.all()
#	html_string = render_to_string('pdf_template2.html', {'jornadas': jornadas})
#	html = HTML(string=html_string)
#	result = html.write_pdf(target='/tmp/jornadas.pdf')
	
#	fs = FileSystemStorage('/tmp')
#	with fs.open('jornadas.pdf') as pdf:
#		response = HttpResponse(pdf, content_type='application/pdf')
#		response['Content-Disposition'] = 'attachment; filename="jornadas.pdf"'
#		return response
#	return response

#Rotina em desenvolvimento
def exportar_noturno_excel(request):
	#recuperando as jornadas do banco. OBS: apenas as jornadas do mês corrente
	jornadas = Jornada.objects.filter(assiduidade=True).filter(fk_tipo_jornada__carga_horaria__in=[24,48]).order_by('data_jornada','fk_equipe__fk_setor__nome', 'fk_equipe__nome','fk_servidor__nome')
	if jornadas:
		response = HttpResponse(content_type='application/ms-excel')
		response['Content-Disposition'] = 'attachment; filename="adicional-noturno.xls"'

		wb = xlwt.Workbook(encoding='utf-8')
		ws = wb.add_sheet('Adicional')

		# largura das colunas
		ws.col(0).width = 256 * 12
		ws.col(1).width = 256 * 10
		ws.col(2).width = 256 * 30
		ws.col(3).width = 256 * 12
		ws.col(4).width = 256 * 50
		ws.col(5).width = 256 * 15
		ws.col(6).width = 256 * 12
		ws.col(7).width = 256 * 12
		ws.col(8).width = 256 * 25
		
		# Sheet header, first row
		row_num = 0

		font_style = xlwt.XFStyle()
		font_style.font.bold = True

		columns = ['NUMFUNC', 'NUMVINC', 'CARGO', 'CPF', 'NOME', 'QUANT(HORAS)', 'DINI', 'DTFIM', 'OBS']

		for col_num in range(len(columns)):
			ws.write(row_num, col_num, columns[col_num], font_style)

		# Sheet body, remaining rows
		font_style = xlwt.XFStyle()

		def setRow(jornada, hora, dt):
			ws.write(row_num, 0, jornada.fk_servidor.id_matricula, font_style)
			ws.write(row_num, 1, jornada.fk_servidor.vinculo, font_style)
			ws.write(row_num, 2, jornada.fk_servidor.cargo, font_style)
			ws.write(row_num, 3, jornada.fk_servidor.cpf, font_style)
			ws.write(row_num, 4, jornada.fk_servidor.nome, font_style)
			ws.write(row_num, 5, hora, font_style)
			ws.write(row_num, 6, dt, font_style)
			ws.write(row_num, 7, dt, font_style)
			ws.write(row_num, 8, "", font_style)

		#calculo do add
		for jornada in jornadas:
			if jornada.fk_tipo_jornada.carga_horaria == 24:
				if jornada.data_jornada.month==Date.today().month:
					row_num += 1
					setRow(jornada, 2,jornada.data_jornada.strftime("%d/%m/%Y"))
				if Date.fromordinal(jornada.data_jornada.toordinal()+1).month==Date.today().month:
					row_num += 1
					setRow(jornada, 5,Date.fromordinal(jornada.data_jornada.toordinal()+1).strftime("%d/%m/%Y"))			
			elif jornada.fk_tipo_jornada.carga_horaria == 48:
				if jornada.data_jornada.month==Date.today().month:
					row_num += 1
					setRow(jornada, 2,jornada.data_jornada.strftime("%d/%m/%Y"))
				if Date.fromordinal(jornada.data_jornada.toordinal()+1).month==Date.today().month:
					row_num += 1
					setRow(jornada, 7,Date.fromordinal(jornada.data_jornada.toordinal()+1).strftime("%d/%m/%Y"))
				if Date.fromordinal(jornada.data_jornada.toordinal()+2).month==Date.today().month:
					row_num += 1
					setRow(jornada, 5,Date.fromordinal(jornada.data_jornada.toordinal()+2).strftime("%d/%m/%Y"))
		wb.save(response)
		return response
	messages.warning(request, 'Ops! Não há jornadas registradas no mês corrente, para o cálculo do adicional noturno!')
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))