'''import json
from django.shortcuts import render
from namp.models import Regiao

def regioes(request):
	#todas as instâncias de Setor do banco de dados
	queryset = Regiao.objects.all()
	regioes = ['Região ' + str(obj.id_regiao) for obj in queryset]
	setores = [int(obj.setor_set.count()) for obj in queryset]
	
	context = {
		'regioes': json.dumps(regioes),
		'setores': json.dumps(setores),
	}
	return render(request, 'admin/namp/regiao/change_list.html', context)'''
