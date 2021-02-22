from django.db import models

# Create your models here.
'''CLASSES SEM CHAVE ESTRANGEIRA'''

class Regiao(models.Model):
	id_regiao = models.AutoField(primary_key=True)
	nome = models.CharField(max_length=100)
	def __str__(self):
		return str(self.id_regiao)
	class Meta:
		verbose_name = "Região"
		verbose_name_plural = "Regiões"

class Funcao(models.Model):
	id_funcao = models.CharField(primary_key=True, max_length=25) #Cod com a secad
	nome = models.CharField(max_length=100)
	def __str__(self):
		return str(self.id_regiao)
	class Meta:
		verbose_name = "Função"
		verbose_name_plural = "Funções"

class EnderecoSetor(models.Model):
	id_endereco_setor = models.AutoField(primary_key=True)
	uf = models.CharField(max_length=2)
	cep = models.CharField(max_length=8)
	municipio = models.CharField(max_length=100)
	endereco = models.CharField(max_length=100)
	numero = models.CharField(max_length=10)
	bairro = models.CharField(max_length=100)
	complemento = models.CharField(max_length=100, blank=True)
	class Meta:
		verbose_name = "Endereço do Setor"
		verbose_name_plural = "Enderecos dos Setores"

class EnderecoServ(models.Model):
	id_endereco_serv = models.AutoField(primary_key=True)
	uf = models.CharField(max_length=2) 
	cep = models.CharField(max_length=8)
	municipio = models.CharField(max_length=100)
	endereco = models.CharField(max_length=100)
	numero = models.CharField(max_length=10)
	bairro = models.CharField(max_length=100)
	complemento = models.CharField(max_length=100, blank=True)
	class Meta:
		verbose_name = "Endereço do Servidor"
		verbose_name_plural = "Endereços de Servidores"

class Afastamento(models.Model):
	id_afastamento = models.CharField('Código', primary_key=True, max_length=25) #Cod com a secad
	tipificacao = models.CharField('Tipo de afastamento', max_length=50)
	descricao = models.CharField(max_length=100)
	class Meta:
		verbose_name = "Afastamento"
		verbose_name_plural = "Afastamentos"

class TipoJornada(models.Model):
	id_tipo_jornada = models.AutoField(primary_key=True)
	carga_horaria = models.PositiveIntegerField()
	tipificacao = models.CharField(max_length=100)
	descricao = models.CharField(max_length=100)
	def __str__(self):
		return str(self.id_tipo_jornada)
	class Meta:
		verbose_name = "Tipo de Jornada"
		verbose_name_plural = "Tipos de Jornadas"

class StatusFuncional(models.Model):
	id_status_funcional = models.AutoField(primary_key=True)
	nome_status = models.CharField(max_length=50)
	descricao_status = models.CharField(max_length=100)
	def __str__(self):
		return self.nome_status	
	class Meta:
		verbose_name = "Status Funcional"
		verbose_name_plural = "Status Funcionais"

''' CLASSES COM CHAVE ESTRANGEIRA'''

'''OneToOneField =1..1
   Foreignkey = 1..*
   ManyToManyField = *..*

   SET_DEFAULT = se apagado a referencia, vai pra outra tabela determinada
'''

class Setor(models.Model):
	id_setor = models.CharField('Código', primary_key=True, max_length=50)
	nome = models.CharField(max_length=100)
	status = models.BooleanField(default=False)
	setor_sede = models.BooleanField(default=False)
	#RESTRICT: proibe a exclussão de região referenciada em setor
	fk_regiao = models.ForeignKey(Regiao, on_delete = models.RESTRICT, verbose_name='Região')
	#CASCATE: se excluido o setor, será excluido o objeto referenciado(endereco_setor)
	fk_endereco_setor = models.OneToOneField(EnderecoSetor, on_delete = models.RESTRICT, verbose_name='Endereço')
	def __str__(self):
		return self.nome
	class Meta:
		verbose_name = "Setor"
		verbose_name_plural = "Setores"

class Equipe(models.Model):
	id_equipe = models.AutoField(primary_key=True)
	nome = models.CharField(max_length=50)
	status = models.BooleanField(default=False)
	hora_inicial = models.TimeField(auto_now= False, auto_now_add=False)
	categoria = models.CharField(max_length=50)
	fk_setor = models.ForeignKey(Setor, on_delete = models.RESTRICT, verbose_name='Setor')
	def __str__(self):
		return self.nome 
	class Meta:
		verbose_name = "Equipe"
		verbose_name_plural = "Equipes"

class ContatoEquipe(models.Model):
	CELULAR = 'Telefone Celular'
	FIXO = 'Telefone Fixo'
	EMAIL = 'E-mail'

	CONTATOS_CHOICES = (
	    (CELULAR,'Telefone Celular'),
	    (FIXO,'Telefone Fixo'),
	    (EMAIL,'E-mail'),
	)

	id_contato_equipe = models.AutoField(primary_key=True)
	tipificacao = models.CharField('Tipo de contato', max_length=50, choices=CONTATOS_CHOICES)
	contato = models.CharField(max_length=50)
	fk_equipe = models.ForeignKey(Equipe, on_delete = models.RESTRICT, verbose_name='Equipe')
	class Meta:
		verbose_name = "Contato da Equipe"
		verbose_name_plural = "Contato das Equipes"

class Servidor(models.Model):
	id_matricula = models.CharField('Matrícula', primary_key=True, max_length=30)
	vinculo = models.CharField(max_length=3) #Parte da matricula
	nome = models.CharField(max_length=100)
	cpf = models.CharField(max_length=11)
	sexo = models.CharField(max_length=1)
	dt_nasc = models.DateField()
	cargo = models.CharField(max_length=50)
	tipo_vinculo = models.CharField(max_length=50)
	regime_juridico = models.CharField(max_length=50)
	situacao = models.BooleanField(default=False)
	fk_equipe = models.ForeignKey(Equipe, on_delete = models.RESTRICT, verbose_name='Equipe')
	fk_endereco_serv = models.OneToOneField(EnderecoServ, on_delete = models.RESTRICT, verbose_name='Endereço')
	def __str__(self):
		return self.id_matricula
	class Meta:
		verbose_name = "Servidor"
		verbose_name_plural = "Servidores"

class HistFuncao(models.Model):
	id_hist_funcao = models.AutoField(primary_key=True)
	data_inicio = models.DateField()
	data_final = models.DateField()
	fk_funcao = models.ForeignKey(Funcao, on_delete = models.RESTRICT, verbose_name='Função')
	fk_servidor = models.ForeignKey(Servidor, on_delete = models.RESTRICT, verbose_name='Servidor')
	def __str__(self):
		return str(self.id_matricula)
	class Meta:
		verbose_name = "Histórico de Função"
		verbose_name_plural = "Históricos de Funcões"

class ContatoServ(models.Model):
	CELULAR = 'Telefone Celular'
	FIXO = 'Telefone Fixo'
	EMAIL = 'E-mail'

	CONTATOS_CHOICES = (
	    (CELULAR,'Telefone Celular'),
	    (FIXO,'Telefone Fixo'),
	    (EMAIL,'E-mail'),
	)

	id_contato_serv = models.AutoField(primary_key=True)
	tipo_contato = models.CharField(max_length=100,choices=CONTATOS_CHOICES)
	contato = models.CharField(max_length=100)
	fk_servidor = models.ForeignKey(Servidor, on_delete = models.RESTRICT)
	def __str__(self):
		return str(self.id_contato_serv)
	class Meta:
		verbose_name = "Contato do Servidor"
		verbose_name_plural = "Contatos de Servidores"

class HistAfastamento(models.Model):
	id_hist_afastamento = models.AutoField(primary_key=True)
	data_inicial = models.DateField()
	duracao = models.PositiveIntegerField()
	fk_afastamento = models.ForeignKey(Afastamento, on_delete = models.RESTRICT, verbose_name='Afastamento')
	fk_servidor = models.ForeignKey(Servidor, on_delete = models.RESTRICT, verbose_name='Servidor')
	def __str__(self):
		return str(self.id_hist_afastamento)
	class Meta:
		verbose_name = "Histório de Afastamento"
		verbose_name_plural = "Históricos de Afastamentos"

class HistLotacao(models.Model):
	id_hist_lotacao = models.AutoField(primary_key=True)
	data_inicial =	models.DateField()
	data_final = models.DateField()
	fk_servidor = models.ForeignKey(Servidor, on_delete = models.RESTRICT, verbose_name='Servidor')
	fk_equipe = models.ForeignKey(Equipe, on_delete = models.RESTRICT, verbose_name='Equipe')
	def __str__(self):
		return str(self.id_hist_lotacao)
	class Meta:
		verbose_name = "Histórico de Lotação"
		verbose_name_plural = "Históricos de Lotações"

class HistStatusFuncional(models.Model):
	id_hist_funcional = models.AutoField(primary_key=True)
	data_inicial = models.DateField()
	data_final = models.DateField()
	fk_servidor = models.ForeignKey(Servidor, on_delete = models.RESTRICT, verbose_name='Servidor')
	fk_status_funcional = models.ForeignKey(StatusFuncional, on_delete = models.RESTRICT, verbose_name='Status Funcional')
	def __str__(self):
		return str(self.id_hist_funcional)
	class Meta:
		verbose_name = "Histórico de Status Funcional"
		verbose_name_plural = "Histórico de Status Funcionais"

class Jornada(models.Model):
	id_jornada = models.AutoField(primary_key=True)
	data_jornada = models.DateField()
	assiduidade = models.BooleanField(default=False)
	fk_servidor = models.ForeignKey(Servidor, on_delete = models.RESTRICT, verbose_name='Servidor')
	fk_equipe = models.ForeignKey(Equipe, on_delete = models.RESTRICT, verbose_name='Equipe')
	fk_tipo_jornada = models.ForeignKey(TipoJornada, on_delete = models.RESTRICT, verbose_name='Tipo Jornada')
	class Meta:
		verbose_name = "Jornada"
		verbose_name_plural = "Jornadas"
