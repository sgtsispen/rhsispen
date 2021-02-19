from django.contrib import admin

# Register your models here.
from django.contrib import admin

from namp.models import Afastamento, ContatoEquipe, ContatoServ, EnderecoServ, EnderecoSetor, Equipe, Funcao, HistAfastamento, HistFuncao, HistLotacao, HistStatusFuncional, Jornada, Regiao, Servidor, Setor, StatusFuncional, TipoJornada

# Register your models here.
class AfastamentoAdmin(admin.ModelAdmin):
	pass
admin.site.register(Afastamento, AfastamentoAdmin)

class ContatoEquipeAdmin(admin.ModelAdmin):
	pass
admin.site.register(ContatoEquipe, ContatoEquipeAdmin)

class ContatoServAdmin(admin.ModelAdmin):
	pass
admin.site.register(ContatoServ, ContatoServAdmin)

class EnderecoServAdmin(admin.ModelAdmin):
	pass
admin.site.register(EnderecoServ, EnderecoServAdmin)

class EnderecoSetorAdmin(admin.ModelAdmin):
	pass
admin.site.register(EnderecoSetor, EnderecoSetorAdmin)

class EquipeAdmin(admin.ModelAdmin):
	pass
admin.site.register(Equipe, EquipeAdmin)

class FuncaoAdmin(admin.ModelAdmin):
	pass
admin.site.register(Funcao, FuncaoAdmin)

class HistAfastamentoAdmin(admin.ModelAdmin):
	pass
admin.site.register(HistAfastamento, HistAfastamentoAdmin)

class HistFuncaoAdmin(admin.ModelAdmin):
	pass
admin.site.register(HistFuncao, HistFuncaoAdmin)

class HistLotacaoAdmin(admin.ModelAdmin):
	pass
admin.site.register(HistLotacao, HistLotacaoAdmin)

class HistStatusFuncionalAdmin(admin.ModelAdmin):
	pass
admin.site.register(HistStatusFuncional, HistStatusFuncionalAdmin)

class JornadaAdmin(admin.ModelAdmin):
	pass
admin.site.register(Jornada, JornadaAdmin)

class RegiaoAdmin(admin.ModelAdmin):
	pass
admin.site.register(Regiao, RegiaoAdmin)

class ServidorAdmin(admin.ModelAdmin):
	pass
admin.site.register(Servidor, ServidorAdmin)

class SetorAdmin(admin.ModelAdmin):
	pass
admin.site.register(Setor, SetorAdmin)

class StatusFuncionalAdmin(admin.ModelAdmin):
	pass
admin.site.register(StatusFuncional, StatusFuncionalAdmin)

class TipoJornadaAdmin(admin.ModelAdmin):
	pass
admin.site.register(TipoJornada, TipoJornadaAdmin)


