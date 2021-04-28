from django import forms
from .models import TipoJornada, Setor, Equipe
from functools import partial

DateInput = partial(forms.DateInput, {'class': 'datepicker'})


class DefinirJornadaRegularForm(forms.Form):
		
	setor = forms.CharField(required=False, label='Código da Unidade')
	data_inicial = forms.DateField(widget=DateInput(),required=True)	
	data_final = forms.DateField(widget=DateInput(),required=True)	
	# o tipo de jornada define a escala sob qual deve ser gerada a joranada
	equipe = forms.ChoiceField()
	tipo_jornada = forms.ChoiceField()

	def __init__(self, *args, **kwargs):
		super(DefinirJornadaRegularForm, self).__init__(*args, **kwargs)
		self.fields['setor'].widget.attrs['readonly'] = True
		self.fields['data_inicial'].widget.attrs['readonly'] = True
		self.fields['data_final'].widget.attrs['readonly'] = True
		self.fields['equipe'].choices = [('', '--Selecione--')] + list(Equipe.objects.all().values_list('id_equipe', 'nome'))
		self.fields['tipo_jornada'].choices = [('', '--Selecione--')] + list(TipoJornada.objects.all().values_list('carga_horaria', 'tipificacao'))