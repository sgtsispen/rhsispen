# Register your models here.
from django.core import serializers
import json
from django import forms
from django.contrib import admin
from django.core.serializers.json import DjangoJSONEncoder
from namp.models import Afastamento, ContatoEquipe, ContatoServ, EnderecoServ, EnderecoSetor, Equipe, Funcao, HistAfastamento, HistFuncao, HistLotacao, HistStatusFuncional, Jornada, Regiao, Servidor, Setor, StatusFuncional, TipoJornada

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
from django_object_actions import DjangoObjectActions
from django.db.models import Count
from django.core.exceptions import ValidationError
# Register your models here.

@admin.register(Afastamento)
class AfastamentoAdmin(admin.ModelAdmin):
	list_display = ('id_afastamento','__str__','descricao')
	#inlines = [descricaoInline]

class ContatoEquipeInline(admin.TabularInline):
    model = ContatoEquipe
    extra = 0
	#def __str__(self):
	#	return ''

class ContatoServInline(admin.TabularInline):
    model = ContatoServ
    extra = 0

class EnderecoServInline(admin.StackedInline):
	model=EnderecoServ
	fieldsets = (
		(None, {
			'fields': (('uf', 'municipio'), 'cep', ('endereco', 'bairro'), ('numero', 'complemento'))
	            }),
	)

class ServidorInline(admin.TabularInline):
	model=Servidor
	fields = ('nome', 'id_matricula','cpf', 'cargo')
	readonly_fields = ('nome', 'id_matricula','cpf', 'cargo')

	def has_add_permission(self, request, obj=None):
		return False

	def has_delete_permission(self, request, obj=None):
		return False

@admin.register(Equipe)
class EquipeAdmin(admin.ModelAdmin):
	list_display = ('nome', 'fk_setor', 'status','hora_inicial','categoria', 'get_servidor')
	list_filter = ('categoria',)
	search_fields = ['nome']
	inlines=[ContatoEquipeInline, ServidorInline]
	
	def get_servidor(self, obj):
		return Servidor.objects.filter(fk_equipe=obj).count()
	get_servidor.short_description = 'Servidores'  #Renames column head
	get_servidor.admin_order_field = 'nome'

class EquipeInline(admin.TabularInline):
	model = Equipe
	extra = 0

@admin.register(Funcao)
class FuncaoAdmin(admin.ModelAdmin):
	list_display = ('id_funcao', 'nome')

@admin.register(HistAfastamento)
class HistAfastamentoAdmin(admin.ModelAdmin):
	search_fields = ('fk_afastamento__tipificacao','fk_servidor__nome', 'fk_afastamento__id_afastamento')
	list_display = ('id_hist_afastamento','data_inicial','data_final','fk_afastamento','fk_servidor')

@admin.register(HistFuncao)
class HistFuncaoAdmin(admin.ModelAdmin):
	search_fields = ('fk_servidor__nome','fk_funcao__nome')
	list_display = ('id_hist_funcao','data_inicio','data_final','fk_funcao','fk_servidor')

@admin.register(HistLotacao)
class HistLotacaoAdmin(admin.ModelAdmin):
	change_form_template = 'admin/namp/histlotacao/change_form.html'
	search_fields = ('fk_servidor__nome','fk_equipe__nome', 'fk_equipe__fk_setor__nome')
	list_display = ('id_hist_lotacao','data_inicial','data_final','fk_servidor','fk_equipe', 'fk_setor')	

@admin.register(HistStatusFuncional)
class HistStatusFuncionalAdmin(admin.ModelAdmin):
	list_display = ('id_hist_funcional','data_inicial', 'data_final', 'fk_servidor', 'fk_status_funcional')

@admin.register(Jornada)
class JornadaAdmin(admin.ModelAdmin):
	change_form_template = 'admin/namp/jornada/change_form.html'

	list_filter = ('assiduidade','fk_equipe','fk_tipo_jornada')
	list_display = ('data_jornada','fk_servidor', 'assiduidade','fk_equipe', 'fk_tipo_jornada')

@admin.register(Regiao)
class RegiaoAdmin(admin.ModelAdmin):
	change_list_template = 'admin/namp/regiao/change_list.html'
	list_display = ('id_regiao','nome', 'get_setor_count')

	def get_setor_count(self, obj):
		return Setor.objects.filter(fk_regiao=obj, status=True).count()
	get_setor_count.short_description = 'Setores'  #Renames column head

	def changelist_view(self, request, extra_context=None):
		#todas as instâncias de Setor do banco de dados
		queryset = Regiao.objects.all()
		regioes = ['Região ' + str(obj.id_regiao) for obj in queryset]
		setores = [int(obj.setor_set.count()) for obj in queryset]

		regioes_json = json.dumps(list(regioes), cls=DjangoJSONEncoder)
		setores_json = json.dumps(list(setores), cls=DjangoJSONEncoder)

		extra_context = extra_context or {"regioes": regioes_json, "setores": setores_json}

		return super().changelist_view(request,extra_context=extra_context)

@admin.register(Servidor)
class ServidorAdmin(DjangoObjectActions, admin.ModelAdmin):	
	change_form_template = 'admin/namp/servidor/change_form.html'
	change_list_template = 'admin/namp/servidor/change_list.html'

	list_per_page = 8
	search_fields = ('nome','fk_equipe__nome', 'fk_equipe__fk_setor__nome')
	radio_fields = {'sexo': admin.HORIZONTAL, 'regime_juridico': admin.HORIZONTAL, 'tipo_vinculo': admin.VERTICAL}
	'''
	Abaixo: apresentação dos forms da model ContatoServ dentro do form da model Servidor
	'''
	list_display = ('nome', 'id_matricula', 'vinculo','cpf','dt_nasc','cargo','tipo_vinculo','regime_juridico','situacao', 'fk_equipe', 'get_setor')
	list_filter = ('cargo','situacao','fk_equipe')
	fieldsets = (
		('Dados Pessoais',{
				'fields': (('nome','cpf'), ('sexo','dt_nasc'))
		}),
		('Dados Funcionais',{
				'fields': (('id_matricula','vinculo'), ('tipo_vinculo', 'regime_juridico'), ('cargo', 'situacao'),'fk_setor', 'fk_equipe')
		}),
	)

	inlines = [EnderecoServInline, ContatoServInline]

	def change_view(self, request, object_id, form_url='', extra_context=None):
		try:
			return super(ServidorAdmin, self).change_view(request, object_id, form_url, extra_context)
		except ValidationError as e:
			return handle_exception(self, request, e)

	def get_setor(self, obj):
		return Setor.objects.get(id_setor=obj.fk_equipe.fk_setor.id_setor)
	get_setor.short_description = 'Unidade Operacional'  #Renames column head
	get_setor.admin_order_field = 'nome'

class EnderecoSetorInline(admin.StackedInline):
	model = EnderecoSetor
	fieldsets = (
		(None, {
			'fields': (('uf', 'municipio'), 'cep', ('endereco', 'bairro'), ('numero', 'complemento'))
	            }),
	)

@admin.register(Setor)
class SetorAdmin(admin.ModelAdmin):
	list_per_page = 8
	list_filter = ('fk_regiao','status','setor_sede',)
	list_display = ('id_setor', 'nome','fk_regiao','status', 'setor_sede', 'get_total_servidor')
	search_fields = ('nome','fk_regiao__nome', 'id_setor')
	inlines = [EnderecoSetorInline,EquipeInline]
	#search_fields = ['nome']

	def get_total_servidor(self, obj):
		return Servidor.objects.filter(fk_equipe__in=Equipe.objects.filter(fk_setor=obj)).count() #total servidores do setor
	get_total_servidor.short_description = 'Servidores'  #Nome da coluna
	get_total_servidor.admin_order_field = 'nome'

@admin.register(StatusFuncional)
class StatusFuncionalAdmin(admin.ModelAdmin):
	list_display = ('nome','descricao')

@admin.register(TipoJornada)
class TipoJornadaAdmin(admin.ModelAdmin):
	list_display = ('carga_horaria', 'tipificacao', 'descricao')