from django.contrib import admin

# Register your models here.
from django.contrib import admin

from namp.models import Afastamento, ContatoEquipe, ContatoServ, EnderecoServ, EnderecoSetor, Equipe, Funcao, HistAfastamento, HistFuncao, HistLotacao, HistStatusFuncional, Jornada, Regiao, Servidor, Setor, StatusFuncional, TipoJornada

# Register your models here.
class AfastamentoAdmin(admin.ModelAdmin):
	pass
	list_display = ('id_afastamento','__str__','descricao')
admin.site.register(Afastamento, AfastamentoAdmin)

class ContatoEquipeAdmin(admin.ModelAdmin):
	pass
	list_display = ('id_contato_equipe','contato', 'fk_equipe')
admin.site.register(ContatoEquipe, ContatoEquipeAdmin)

class ContatoServAdmin(admin.ModelAdmin):
	pass
	list_display = ('id_contato_serv','contato', 'fk_servidor')
admin.site.register(ContatoServ, ContatoServAdmin)

class EnderecoServAdmin(admin.ModelAdmin):
	pass
admin.site.register(EnderecoServ, EnderecoServAdmin)

class EnderecoSetorAdmin(admin.ModelAdmin):
	pass
admin.site.register(EnderecoSetor, EnderecoSetorAdmin)

class EquipeAdmin(admin.ModelAdmin):
	pass
	list_display = ('id_equipe','nome','status','hora_inicial','categoria','fk_setor')
admin.site.register(Equipe, EquipeAdmin)

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
	list_display = ('id_jornada','data_jornada','assiduidade','fk_servidor','fk_equipe','fk_tipo_jornada')
admin.site.register(Jornada, JornadaAdmin)

class RegiaoAdmin(admin.ModelAdmin):
	pass
	list_display = ('id_regiao','nome')
admin.site.register(Regiao, RegiaoAdmin)

class ServidorAdmin(admin.ModelAdmin):
	pass
	list_display = ('__str__','vinculo', 'cpf', 'sexo','dt_nasc','cargo','tipo_vinculo','regime_juridico','situacao','fk_equipe','fk_endereco_serv')
admin.site.register(Servidor, ServidorAdmin)

class SetorAdmin(admin.ModelAdmin):
	pass
	list_display = ('nome','setor_sede','fk_regiao','fk_endereco_setor')
admin.site.register(Setor, SetorAdmin)

class StatusFuncionalAdmin(admin.ModelAdmin):	
	pass
	list_display = ('id_status_funcional','__str__','descricao_status')
admin.site.register(StatusFuncional, StatusFuncionalAdmin)

class TipoJornadaAdmin(admin.ModelAdmin):
	pass
	list_display = ('id_tipo_jornada','carga_horaria', 'tipificacao', 'descricao')
admin.site.register(TipoJornada, TipoJornadaAdmin)