# Register your models here.
from django.core import serializers
import json
from django import forms
from django.contrib import admin
from django.core.serializers.json import DjangoJSONEncoder

from namp.forms import ServidorFormAdmin, EnderecoFormAdmin, TextFormAdmin, HoraFormAdmin, HistStatusFuncionalFormAdmin, HistAfastamentoFormAdmin  # Formulario para mascara
from namp.models import (Afastamento, ContatoEquipe, ContatoServ, EnderecoServ,
                         EnderecoSetor, Equipe, Funcao, HistAfastamento,
                         HistFuncao, HistLotacao, HistStatusFuncional, Jornada,
                         Regiao, Servidor, Setor, StatusFuncional, TipoJornada)
#PDF
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.core.files.storage import FileSystemStorage
from weasyprint import HTML
from django_object_actions import DjangoObjectActions
from django.template.loader import render_to_string

# Register your models here.
class AfastamentoAdmin(admin.ModelAdmin):
	form = TextFormAdmin
	list_display = ('id_afastamento','__str__','descricao')
admin.site.register(Afastamento, AfastamentoAdmin)

class ContatoEquipeInline(admin.TabularInline):
    model = ContatoEquipe
    extra = 0

class ContatoServInline(admin.TabularInline):
	#form = ContatoFormAdmin
	model = ContatoServ
	extra = 0

class EnderecoServInline(admin.StackedInline):
	form = EnderecoFormAdmin
	model= EnderecoServ
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

class EquipeAdmin(admin.ModelAdmin):
	form = HoraFormAdmin
	list_display = ('nome', 'fk_setor', 'status','hora_inicial','categoria', 'get_servidor')
	list_filter = ('categoria', )
	inlines=[ContatoEquipeInline, ServidorInline]
	search_fields = ['nome']
	autocomplete_fields = ['fk_setor']
	def get_servidor(self, obj):
		return Servidor.objects.filter(fk_equipe=obj).count()
	get_servidor.short_description = 'Servidores'  #Nome da coluna 
	get_servidor.admin_order_field = 'nome'		   #Ordem da coluna

	class Media: #IMPORTAR ARQUIVO JS MASK
		js = (
			"jquery.mask.min.js",
			"mascara.js",
			)

admin.site.register(Equipe, EquipeAdmin)

class EquipeInline(admin.TabularInline):
	model = Equipe
	extra = 0

class FuncaoAdmin(admin.ModelAdmin):
	list_display = ('id_funcao', 'nome')
admin.site.register(Funcao, FuncaoAdmin)

class HistAfastamentoAdmin(admin.ModelAdmin):
	form =  HistAfastamentoFormAdmin
	search_fields = ('fk_servidor__nome',)  #campo de busca por nome do servidor
	list_per_page = 8						#limita a quantidade de info na pág
	list_display = ('id_hist_afastamento','data_inicial','data_final','fk_afastamento','fk_servidor')
	class Media: #IMPORTAR ARQUIVO JS MASK
		js = (
			"jquery.mask.min.js",
			"mascara.js",
			)
admin.site.register(HistAfastamento, HistAfastamentoAdmin)

class HistFuncaoAdmin(admin.ModelAdmin):
	search_fields = ('fk_servidor__nome',) 
	list_per_page = 8
	list_display = ('id_hist_funcao','data_inicio','data_final','fk_funcao','fk_servidor')
admin.site.register(HistFuncao, HistFuncaoAdmin)

class HistLotacaoAdmin(admin.ModelAdmin):
	search_fields = ('fk_servidor__nome',)
	list_per_page = 8
	list_display = ('fk_servidor','data_inicial','data_final','fk_equipe', 'get_setor')
	list_filter = ('fk_equipe__nome', )
	def get_setor(self, obj):
		return Setor.objects.get(id_setor=obj.fk_equipe.fk_setor.id_setor)
	get_setor.short_description = 'Unidade Operacional'  #Nome da coluna
	get_setor.admin_order_field = 'fk_servidor'

admin.site.register(HistLotacao, HistLotacaoAdmin)

class HistStatusFuncionalAdmin(admin.ModelAdmin):
	form = HistStatusFuncionalFormAdmin
	search_fields = ('fk_servidor__nome',)
	list_per_page = 8
	list_display = ('id_hist_funcional','data_inicial', 'data_final', 'fk_servidor', 'fk_status_funcional')

	#autocomplete_fields = ['fk_servidor']
	#autocomplete_fields = ['fk_status_funcional']
	class Media: #IMPORTAR ARQUIVO JS MASK
		js = (
			"jquery.mask.min.js",
			"mascara.js",
			)

admin.site.register(HistStatusFuncional, HistStatusFuncionalAdmin)

class JornadaAdmin(admin.ModelAdmin):
	#autocomplete_fields = ["fk_servidor"]
	list_filter = ('assiduidade','fk_equipe','fk_tipo_jornada')
	list_display = ('data_jornada','fk_servidor', 'assiduidade','fk_equipe', 'fk_tipo_jornada')

	def formfield_for_foreignkey(self, db_field, request, **kwargs):
		if db_field.name == "fk_equipe":
			kwargs["queryset"] = Equipe.objects.none()		
		return super(JornadaAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
admin.site.register(Jornada, JornadaAdmin)

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
admin.site.register(Regiao, RegiaoAdmin)

@admin.register(Servidor)
class ServidorAdmin(DjangoObjectActions, admin.ModelAdmin):
	form = ServidorFormAdmin #Add para as mascaras

	#change_form_template = 'admin/namp/servidor/change_form.html'
	#change_list_template = 'admin/namp/servidor/change_list.html'

	list_per_page = 8
	search_fields = ('nome','fk_equipe__nome', 'fk_equipe__fk_setor__nome')
	#autocomplete_fields = ['fk_setor']
	radio_fields = {'sexo': admin.HORIZONTAL, 'regime_juridico': admin.HORIZONTAL}
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

	def formfield_for_foreignkey(self, db_field, request, **kwargs):
		if db_field.name == "fk_equipe":
			kwargs["queryset"] = Equipe.objects.order_by('nome').values_list('nome', flat=True).distinct()
		return super(ServidorAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

	def get_setor(self, obj):
		return Setor.objects.get(id_setor=obj.fk_equipe.fk_setor.id_setor)
	get_setor.short_description = 'Unidade Operacional' 
	get_setor.admin_order_field = 'nome'
#admin.site.register(Servidor, ServidorAdmin)


class EnderecoSetorInline(admin.StackedInline):
	form = EnderecoFormAdmin
	model = EnderecoSetor
	fieldsets = (
		(None, {
			'fields': (('uf', 'municipio'), 'cep', ('endereco', 'bairro'), ('numero', 'complemento'))
	            }),
	)

class SetorAdmin(admin.ModelAdmin):
	list_per_page = 8
	list_filter = ('fk_regiao','status','setor_sede',)
	list_display = ('id_setor', 'nome','fk_regiao','status', 'setor_sede', 'get_total_servidor')
	search_fields = ('nome','fk_regiao__nome', 'id_setor')
	inlines = [EnderecoSetorInline,EquipeInline]
	#search_fields = ['nome']


	def get_total_servidor(self, obj):
		return Servidor.objects.filter(fk_equipe__in=Equipe.objects.filter(fk_setor=obj)).count() #total servidores do setor
	get_total_servidor.short_description = 'Servidores'  
	get_total_servidor.admin_order_field = 'nome'

admin.site.register(Setor, SetorAdmin)

class StatusFuncionalAdmin(admin.ModelAdmin):
	list_display = (str('tipificacao'),'descricao')
admin.site.register(StatusFuncional, StatusFuncionalAdmin)

class TipoJornadaAdmin(admin.ModelAdmin):
	list_display = ('carga_horaria', 'tipificacao', 'descricao')
admin.site.register(TipoJornada, TipoJornadaAdmin)



