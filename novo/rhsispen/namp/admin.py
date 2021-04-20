# Register your models here.
import json

from django.contrib import admin
from django.core.serializers.json import DjangoJSONEncoder
from django import forms
from django.core.exceptions import ObjectDoesNotExist
from namp.models import Afastamento, ContatoEquipe, ContatoServ, EnderecoServ, EnderecoSetor, Equipe, Funcao, HistAfastamento, HistFuncao, HistLotacao, HistStatusFuncional, Jornada, Regiao, Servidor, Setor, StatusFuncional, TipoJornada

# Register your models here.
class AfastamentoAdmin(admin.ModelAdmin):
	pass
	list_display = ('id_afastamento','__str__','descricao')
	#inlines = [descricaoInline]
admin.site.register(Afastamento, AfastamentoAdmin)

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

class EquipeAdmin(admin.ModelAdmin):
	list_display = ('nome', 'fk_setor', 'status','hora_inicial','categoria', 'get_servidor')
	list_filter = ('fk_setor', 'categoria')
	inlines=[ContatoEquipeInline, ServidorInline]
	search_fields = ['nome']
	autocomplete_fields = ['fk_setor']


	def get_servidor(self, obj):
		return Servidor.objects.filter(fk_equipe=obj).count()
	get_servidor.short_description = 'Servidores'  #Renames column head
	get_servidor.admin_order_field = 'nome'

admin.site.register(Equipe, EquipeAdmin)

class EquipeInline(admin.TabularInline):
	model = Equipe
	extra = 0

class FuncaoAdmin(admin.ModelAdmin):
	list_display = ('id_funcao', 'nome')
admin.site.register(Funcao, FuncaoAdmin)

class HistAfastamentoAdmin(admin.ModelAdmin):
	list_display = ('id_hist_afastamento','data_inicial','data_final','fk_afastamento','fk_servidor')
admin.site.register(HistAfastamento, HistAfastamentoAdmin)

class HistFuncaoAdmin(admin.ModelAdmin):
	list_display = ('id_hist_funcao','data_inicio','data_final','fk_funcao','fk_servidor')
admin.site.register(HistFuncao, HistFuncaoAdmin)

class HistLotacaoAdmin(admin.ModelAdmin):
	#def get_servidor(self, obj):
	#	return Servidor.objects.get()

	#search_fields = [get_servidor] #ARRUMAR A BUSCA, FK_SERVIDOR_NAO_FUNCIONA
	list_display = ('id_hist_lotacao','data_inicial','data_final','fk_servidor','fk_equipe', 'get_setor')
	def get_setor(self, obj):
		return Setor.objects.get(id_setor=obj.fk_equipe.fk_setor.id_setor)
	get_setor.short_description = 'Unidade Operacional'  #Nome da coluna
	get_setor.admin_order_field = 'fk_servidor'


admin.site.register(HistLotacao, HistLotacaoAdmin)

class HistStatusFuncionalAdmin(admin.ModelAdmin):
	list_display = ('id_hist_funcional','data_inicial', 'data_final', 'fk_servidor', 'fk_status_funcional')
admin.site.register(HistStatusFuncional, HistStatusFuncionalAdmin)

class JornadaAdmin(admin.ModelAdmin):
	list_filter = ('assiduidade','fk_equipe','fk_tipo_jornada')
	list_display = ('data_jornada','fk_servidor', 'assiduidade','fk_equipe', 'fk_tipo_jornada')
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

class ServidorAdmin(admin.ModelAdmin):
	list_per_page = 8
	search_fields = ('nome','fk_equipe__nome', 'fk_equipe__fk_setor__nome')
	#autocomplete_fields = ['serv_setor']
	radio_fields = {'sexo': admin.HORIZONTAL, 'regime_juridico': admin.HORIZONTAL, 'tipo_vinculo': admin.VERTICAL}
	'''
	Abaixo: apresentação dos forms da model ContatoServ dentro do form da model Servidor
	'''
	list_display = ('nome', 'id_matricula', 'vinculo','cpf','dt_nasc','cargo','tipo_vinculo','regime_juridico','situacao','fk_equipe', 'get_setor')
	list_filter = ('cargo','situacao','fk_equipe')
	fieldsets = (
		('Dados Pessoais',{
				'fields': (('nome','cpf'), ('sexo','dt_nasc'))
		}),
		('Dados Funcionais',{
				'fields': (('id_matricula','vinculo'), ('tipo_vinculo', 'regime_juridico'), ('cargo', 'situacao'),'serv_setor','fk_equipe')
		}),
	)

	inlines = [EnderecoServInline, ContatoServInline]

	my_id_for_formfield = None
	def get_form(self, request, obj=None, **kwargs):
		if obj:
			self.my_id_for_formfield = obj.id
		return super(ServidorAdmin, self).get_form(request, obj, **kwargs)

	def formfield_for_foreignkey(self, db_field, request, **kwargs):
		print(self.my_id_for_formfield)
		if db_field.name == "fk_equipe":
			kwargs["queryset"] = Equipe.objects.filter(fk_setor=self.my_id_for_formfield)
		return super(ServidorAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

	def get_setor(self, obj):
		return Setor.objects.get(id_setor=obj.fk_equipe.fk_setor.id_setor)
	get_setor.short_description = 'Unidade Operacional'  #Renames column head
	get_setor.admin_order_field = 'nome'
admin.site.register(Servidor, ServidorAdmin)

class EnderecoSetorInline(admin.StackedInline):
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

	def get_total_servidor(self, obj):
		return Servidor.objects.filter(fk_equipe__in=Equipe.objects.filter(fk_setor=obj)).count() #total servidores do setor
	get_total_servidor.short_description = 'Servidores'  #Nome da coluna
	get_total_servidor.admin_order_field = 'nome'

admin.site.register(Setor, SetorAdmin)

class StatusFuncionalAdmin(admin.ModelAdmin):
	list_display = (str('tipificacao'),'descricao')
admin.site.register(StatusFuncional, StatusFuncionalAdmin)

class TipoJornadaAdmin(admin.ModelAdmin):
	list_display = ('carga_horaria', 'tipificacao', 'descricao')
admin.site.register(TipoJornada, TipoJornadaAdmin)
