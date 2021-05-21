from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from namp.models import Servidor, HistLotacao, HistAfastamento, Jornada
import datetime

'''
	Este Signal popula a tabela HistLotação sempre que uma
	instância de Servidor for criada ou modificada. No entanto,
	havendo modificação de uma instância de Servidor, o HistLoação
	anterior é atualizado com a data atual e o novo HistLotação é
	criado.
'''
@receiver(post_save, sender=Servidor)
def post_save_create_histlotacao(sender, instance, created, **kargs):
	if created:
		HistLotacao.objects.create(
			data_inicial=datetime.date.today(),
			fk_servidor=instance,
			fk_setor=instance.fk_setor,
			fk_equipe=instance.fk_equipe)
	else:
		print('Servidor foi alterado.')	
		try:
			print('Buscando lotação do servidor.')	
			oldHistLotacao = HistLotacao.objects.filter(
				fk_servidor=instance,
				data_final__isnull=True).order_by('-data_inicial').first()
		except HistLotacao.DoesNotExist:
			print('Lotação do servidor não foi encontrada e uma nova foi criada.')
			pass
		else:
			print('Lotação do servidor foi encontrada e alterada.')	
			if oldHistLotacao:
				if oldHistLotacao.fk_setor != instance.fk_setor or oldHistLotacao.fk_equipe != instance.fk_equipe:
					oldHistLotacao.data_final = datetime.date.today()
					oldHistLotacao.save()
					HistLotacao.objects.create(
						data_inicial=datetime.date.today(),
						fk_servidor=instance,
						fk_setor=instance.fk_setor,
						fk_equipe=instance.fk_equipe)
			else:
				HistLotacao.objects.create(
					data_inicial=datetime.date.today(),
					fk_servidor=instance,
					fk_setor=instance.fk_setor,
					fk_equipe=instance.fk_equipe)

'''
'''
@receiver(pre_save, sender=HistAfastamento)
def pre_save_update_jornada(sender, instance, **kargs):
	try:	
		oldHistAfastamento = HistAfastamento.objects.filter(
			id_hist_afastamento=instance.id_hist_afastamento).first()
	except HistAfastamento.DoesNotExist:
		print('Houve uma except!')
		pass
	else:
		print(oldHistAfastamento.id_hist_afastamento,oldHistAfastamento.fk_afastamento)
		print(instance.id_hist_afastamento,instance.fk_afastamento)
		if((oldHistAfastamento.fk_afastamento != instance.fk_afastamento) or
			(oldHistAfastamento.fk_servidor != instance.fk_servidor) or
			(oldHistAfastamento.data_inicial != instance.data_inicial) or
			(oldHistAfastamento.data_final != instance.data_final)):
			try:	
				jornadas = Jornada.objects.filter(
					fk_servidor=oldHistAfastamento.fk_servidor,
					data_jornada__range=[oldHistAfastamento.data_inicial, oldHistAfastamento.data_final])
			except Jornada.DoesNotExist:
				print('Houve uma except!')
				pass
			else:
				if jornadas:
					print(jornadas)
					for jornada in jornadas:
						jornada.assiduidade = True
						print('assiduidade alterada!')
						jornada.fk_afastamento = None
						print('afastamento anulado!')
						jornada.save()
						print('jornada salva!')
'''
	Este Signal desmarca a assiduidade e lança o tipo de afastamento
	nas jornadas existentes dentro do período do afastamento que 
	esteja sendo criado para o servidor vinculado a ele.
'''
@receiver(post_save, sender=HistAfastamento)
def post_save_create_afastamento(sender, instance, created, **kargs):
	if created:
		try:
			jornadas = Jornada.objects.filter(
				fk_servidor=instance.fk_servidor,
				data_jornada__range=[instance.data_inicial, instance.data_final])
		except Jornada.DoesNotExist:
			pass
		else:
			if jornadas:
				for jornada in jornadas:
					jornada.assiduidade = False
					jornada.fk_afastamento = instance.fk_afastamento
					jornada.save()

'''
	Este Signal desmarca a assiduidade e lança o tipo de afastamento
	numa jornada que esteja sendo criada dentro do período de um 
	afastamento já existente para o servidor vinculado a ela.
'''
@receiver(pre_save, sender=Jornada)
def pre_save_create_jornada(sender, instance, **kargs):
	try:
		myHistAfastamento = HistAfastamento.objects.filter(
			fk_servidor=instance.fk_servidor).order_by('-data_inicial').first()
	except HistAfastamento.DoesNotExist:
		pass
	else:
		if myHistAfastamento:
			for	data in range(myHistAfastamento.data_inicial.toordinal(), myHistAfastamento.data_final.toordinal()+1):
				if instance.data_jornada.toordinal() == data:
					instance.assiduidade = False
					instance.fk_afastamento = myHistAfastamento.fk_afastamento