from django.db.models.signals import post_save
from django.dispatch import receiver
from namp.models import Servidor, HistLotacao
import datetime

'''
	Usabilidade de Signals do django

	Populando HistLotacao ao criar uma instância de Servidor, a qual registra a equipe
	do servidor.
	
	create_histlotacao: cria uma instância de histLotacao, assim que um servidor for
	inserido no sistema. A data_final da instância de histLotação fica vazia até que
	o servidor mude de equipe.

	update_histlotacao: a instância anterior do histLotação do servidor vai receber a
	data atual de alteração de sua equipe. Uma nova instância de histLotação será criada,
	configurando a alteração da lotação do servidor.
'''
@receiver(post_save, sender=Servidor)
def create_histlotacao(sender, instance, created, **kargs):
	if created:
		# Criando uma instância de HistLotação, a qual faz referência ao novo servidor criado
		HistLotacao.objects.create(data_inicial=datetime.date.today(), fk_servidor=instance,fk_equipe=instance.fk_equipe)

@receiver(post_save, sender=Servidor)
def update_histlotacao(sender, instance, created, **kargs):
	if created == False:
		# Recuperando a instância de HistLotação já existende, a qual tem o atributo data_final vazio
		oldHistLotacao = HistLotacao.objects.get(fk_servidor=instance, data_final__isnull=True)

		# Verificando se o atributo fk_equipe da instância de Servidor foi editada
		if oldHistLotacao.fk_equipe != instance.fk_equipe:
			# Atribuindo a data final para a atual instância de HistLotacao
			oldHistLotacao.data_final = datetime.date.today()  # Returns 2018-01-15
			oldHistLotacao.save()
			# Criando uma instância de HistLotação, a qual faz referência à instância de Servidor editado
			HistLotacao.objects.create(data_inicial=datetime.date.today(), fk_servidor=instance,fk_equipe=instance.fk_equipe)