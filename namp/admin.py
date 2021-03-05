# Register your models here.
import json

from django.contrib import admin
from django.core.serializers.json import DjangoJSONEncoder

from namp.models import Afastamento, ContatoEquipe, ContatoServ, EnderecoServ, EnderecoSetor, Equipe, Funcao, HistAfastamento, HistFuncao, HistLotacao, HistStatusFuncional, Jornada, Regiao, Servidor, Setor, StatusFuncional, TipoJornada

admin.site.site_header = 'Administração do Núcleo de Apoio a Movimentação de Pessoal'

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

class ContatoEquipeAdmin(admin.ModelAdmin):
	pass
	list_display = ('fk_equipe','contato')
	#get_name.short_description = 'teste'

admin.site.register(ContatoEquipe, ContatoEquipeAdmin)

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
	#extra=0
	#exclude = ['dt_nasc', 'cargo', 'tipo_vinculo', 'regime_juridico', 'fk_endereco_serv', 'situacao']
	fields = ('nome', 'id_matricula','cpf', 'cargo')
	readonly_fields = ('nome', 'id_matricula','cpf', 'cargo')

	def has_add_permission(self, request, obj=None):
		return False
	
	def has_delete_permission(self, request, obj=None):
		return False

class EquipeAdmin(admin.ModelAdmin):
	list_display = ('nome', 'fk_setor', 'status','hora_inicial','categoria')
	list_filter = ('fk_setor', 'categoria')	

	inlines=[ContatoEquipeInline, ServidorInline]
admin.site.register(Equipe, EquipeAdmin)

class EquipeInline(admin.TabularInline):
	model = Equipe
	extra = 0

class FuncaoAdmin(admin.ModelAdmin):
	pass
	list_display = ('id_funcao', 'nome')
admin.site.register(Funcao, FuncaoAdmin)

class HistAfastamentoAdmin(admin.ModelAdmin):
	pass
	list_display = ('id_hist_afastamento','data_inicial','duracao','fk_afastamento','fk_servidor')
admin.site.register(HistAfastamento, HistAfastamentoAdmin)

class HistFuncaoAdmin(admin.ModelAdmin):
	pass
	list_display = ('id_hist_funcao','data_inicio','data_final','fk_funcao','fk_servidor')
admin.site.register(HistFuncao, HistFuncaoAdmin)

class HistLotacaoAdmin(admin.ModelAdmin):
	pass
	list_display = ('id_hist_lotacao','data_inicial','data_final','fk_servidor','fk_equipe')
admin.site.register(HistLotacao, HistLotacaoAdmin)

class HistStatusFuncionalAdmin(admin.ModelAdmin):
	list_display = ('id_hist_funcional','data_inicial', 'data_final', 'fk_servidor', 'fk_status_funcional')
	pass	
admin.site.register(HistStatusFuncional, HistStatusFuncionalAdmin)

class JornadaAdmin(admin.ModelAdmin):
	pass
	list_filter = ('assiduidade','fk_equipe','fk_tipo_jornada')	
	list_display = ('data_jornada','fk_servidor', 'assiduidade','fk_equipe', 'fk_tipo_jornada')
admin.site.register(Jornada, JornadaAdmin)

class RegiaoAdmin(admin.ModelAdmin):
	change_list_template = 'admin/namp/regiao/change_list.html'
	list_display = ('id_regiao','nome')
	
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
	'''
	Abaixo: apresentação dos forms da model ContatoServ dentro do form da model Servidor
	'''	
	search_fields = ('nome',)
	list_display = ('__str__','vinculo','nome', 'cpf', 'sexo','dt_nasc','cargo','tipo_vinculo','regime_juridico','situacao','fk_equipe')
	list_filter = ('cargo','situacao',str('fk_equipe'))
	fieldsets = (
		('Dados Pessoais',{
				'fields': (('nome','cpf'), ('sexo','dt_nasc'))
		}),
		('Dados Funcionais',{
				'fields': ((str('id_matricula'),'vinculo'), ('tipo_vinculo','regime_juridico'), ('cargo', 'situacao'),  str('fk_equipe'))
		}),
	)
	inlines = [EnderecoServInline, ContatoServInline]
admin.site.register(Servidor, ServidorAdmin)

class EnderecoSetorInline(admin.StackedInline):
	model = EnderecoSetor
	fieldsets = (
		(None, {
			'fields': (('uf', 'municipio'), 'cep', ('endereco', 'bairro'), ('numero', 'complemento'))
	            }),
	)

class SetorAdmin(admin.ModelAdmin):
	pass
	list_filter = ('fk_regiao','status','setor_sede',)
	list_display = ('id_setor', 'nome','fk_regiao','status', 'setor_sede')
	search_fields = ('nome',)
	inlines = [EnderecoSetorInline,EquipeInline]
admin.site.register(Setor, SetorAdmin)

class StatusFuncionalAdmin(admin.ModelAdmin):	
	pass
	list_display = (str('nome_status'),'descricao_status')
admin.site.register(StatusFuncional, StatusFuncionalAdmin)

class TipoJornadaAdmin(admin.ModelAdmin):
	pass
	list_display = ('carga_horaria', 'tipificacao', 'descricao')
admin.site.register(TipoJornada, TipoJornadaAdmin)
