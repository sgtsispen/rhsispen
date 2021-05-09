from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from namp.models import Servidor, HistLotacao, HistAfastamento, Jornada
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
def create_histlotacao(sender, instance, **kargs):
	# Criando uma instância de HistLotação, a qual faz referência ao novo servidor criado
	HistLotacao.objects.create(data_inicial=datetime.date.today(), fk_servidor=instance,fk_setor=instance.fk_setor,fk_equipe=instance.fk_equipe)


@receiver(pre_save, sender=Servidor)
def update_histlotacao(sender, instance, **kargs):
	if HistLotacao.objects.filter(fk_servidor=instance, data_final__isnull=True).count() != 0:
		# Recuperando a instância de HistLotação já existende, a qual tem o atributo data_final vazio
		oldHistLotacao = HistLotacao.objects.filter(fk_servidor=instance, data_final__isnull=True).order_by('-data_inicial').first()
				
		# Verificando se o atributo fk_equipe da instância de Servidor foi editada
		if oldHistLotacao.fk_equipe != instance.fk_equipe or oldHistLotacao.fk_setor != instance.fk_setor:
			# Atribuindo a data final para a atual instância de HistLotacao
			oldHistLotacao.data_final = datetime.date.today()  # Returns 2018-01-15
			oldHistLotacao.save()
			# Criando uma instância de HistLotação, a qual faz referência à instância de Servidor editado

@receiver(post_save, sender=HistAfastamento)
def post_save_update_jornada(sender, instance, **kargs):
	jornadas = Jornada.objects.filter(fk_servidor=instance.fk_servidor).filter(data_jornada__range=[instance.data_inicial, instance.data_final])
	if jornadas:
		for jornada in jornadas:
			jornada.assiduidade = False
			jornada.fk_afastamento = instance.fk_afastamento
			jornada.save()

@receiver(pre_save, sender=HistAfastamento)
def pre_save_update_jornada(sender, instance, **kargs):
	if HistAfastamento.objects.filter(fk_servidor=instance.fk_servidor).count() != 0:
		oldHistAfastamento = HistAfastamento.objects.filter(fk_servidor=instance.fk_servidor).order_by('-data_inicial').first()		
		jornadas = Jornada.objects.filter(fk_servidor=oldHistAfastamento.fk_servidor).filter(data_jornada__range=[oldHistAfastamento.data_inicial, oldHistAfastamento.data_final])
		if jornadas:
			for jornada in jornadas:
				jornada.assiduidade = True
				jornada.fk_afastamento = None
				jornada.save()

@receiver(pre_save, sender=Jornada)
def pre_save_create_jornada(sender, instance, **kargs):
	if HistAfastamento.objects.filter(fk_servidor=instance.fk_servidor).count() != 0:
		myHistAfastamento = HistAfastamento.objects.filter(fk_servidor=instance.fk_servidor).order_by('-data_inicial').first()					
		for	data in range(myHistAfastamento.data_inicial.toordinal(), myHistAfastamento.data_final.toordinal()+1):
			if instance.data_jornada.toordinal() == data:
				instance.assiduidade = False
				instance.fk_afastamento = myHistAfastamento.fk_afastamento