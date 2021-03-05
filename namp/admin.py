
import json

from django.contrib import admin
from django.core.serializers.json import DjangoJSONEncoder


from namp.models import Afastamento, ContatoEquipe, ContatoServ, EnderecoServ, EnderecoSetor, Equipe, Funcao, HistAfastamento, HistFuncao, HistLotacao, HistStatusFuncional, Jornada, Regiao, Servidor, Setor, StatusFuncional, TipoJornada

#Cabeçalho da página
admin.site.site_header = 'Administração do Núcleo de Apoio a Movimentação de Pessoal'

# Registro de models
class AfastamentoAdmin(admin.ModelAdmin):
	pass
	list_display = ('id_afastamento','__str__','descricao')
admin.site.register(Afastamento, AfastamentoAdmin)

class ContatoEquipeInline(admin.TabularInline):
    model = ContatoEquipe
    extra = 0

class ContatoEquipeAdmin(admin.ModelAdmin):
	pass
	list_display = ('__str__','contato')
admin.site.register(ContatoEquipe, ContatoEquipeAdmin)
	
class ContatoServInline(admin.TabularInline):
    model = ContatoServ
    extra = 0

class EnderecoServAdmin(admin.ModelAdmin):
	pass
admin.site.register(EnderecoServ, EnderecoServAdmin)

'''
class EnderecoServInline(admin.TabularInline):
	model = EnderecoServ
	extra = 1
'''
class EnderecoSetorAdmin(admin.ModelAdmin):
	pass
	list_display = ('endereco','numero','bairro','complemento','cep','municipio')
admin.site.register(EnderecoSetor, EnderecoSetorAdmin)

class ServidorInline(admin.TabularInline):
    model = Servidor
	#readonly_fields = ('__str__', 'cpf', 'cargo')
    fields = ('nome', str('id_matricula'),'vinculo','cpf', 'cargo') 
    extra = 1

class EquipeAdmin(admin.ModelAdmin):
	pass
	list_display = ('nome','fk_setor','status','hora_inicial','categoria')
	inlines = [ServidorInline]
admin.site.register(Equipe, EquipeAdmin)

class EquipeInline(admin.TabularInline):
	model = Equipe
	extra = 1

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
	pass
	#list_display = ('id_matricula','vinculo','nome','cpf', 'sexo','dt_nasc','cargo','tipo_vinculo','regime_juridico','situacao','fk_equipe','fk_endereco_serv')
	list_display = ('__str__','vinculo', 'cpf', 'sexo','cargo','tipo_vinculo','regime_juridico','situacao','fk_equipe','fk_endereco_serv')
	list_filter = ('cargo','tipo_vinculo','regime_juridico','situacao',str('fk_equipe'),str('fk_endereco_serv'))
	fieldsets = (
		('DADOS PESSOAIS',{
				'fields': ((str('id_matricula'),'vinculo'), 'nome', 'cpf', 'sexo','dt_nasc', str('fk_endereco_serv'))
		}),
		('DADOS FUNCIONAIS',{
				'fields': ('cargo','tipo_vinculo','regime_juridico','situacao', str('fk_equipe'))
		}),
	)
	'''
	Abaixo: apresentação dos forms da model ContatoServ dentro do form da model Servidor
	'''	
	inlines = [ContatoServInline]
	#inlines = [EnderecoServInline] PRONTO PARA RECEBER A CHAVE ESTRANGEIRA
admin.site.register(Servidor, ServidorAdmin)

class EnderecoSetorInline(admin.StackedInline):
	model = EnderecoSetor

class EnderecoSetorAdmin(admin.ModelAdmin):
	list_display = ('endereco','numero','bairro','complemento','cep','municipio')
admin.site.register(EnderecoSetor, EnderecoSetorAdmin)

class SetorAdmin(admin.ModelAdmin):
	pass
	list_filter = ('fk_regiao','status','setor_sede')
	list_display = ('id_setor', 'nome','fk_regiao','fk_endereco_setor','status', 'setor_sede')
	search_fields = ('nome',)
	inlines = [EquipeInline]
admin.site.register(Setor, SetorAdmin)

class StatusFuncionalAdmin(admin.ModelAdmin):	
	pass
	list_display = (str('nome_status'),'descricao_status')
admin.site.register(StatusFuncional, StatusFuncionalAdmin)

class TipoJornadaAdmin(admin.ModelAdmin):
	pass
	list_display = ('carga_horaria', 'tipificacao', 'descricao')
admin.site.register(TipoJornada, TipoJornadaAdmin)

