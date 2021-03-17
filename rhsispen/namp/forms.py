from django import forms
 
class ServidorFormAdmin(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ServidorFormAdmin, self).__init__(*args, **kwargs)
        self.fields['cpf'].widget.attrs['class'] = 'mask-cpf'
        self.fields['dt_nasc'].widget.attrs['class'] = 'mask-dt_nasc'

class EnderecoFormAdmin(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EnderecoFormAdmin, self).__init__(*args, **kwargs)       
        self.fields['cep'].widget.attrs['class'] = 'mask-cep'

class ContatoFormAdmin(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ContatoFormAdmin, self).__init__(*args, **kwargs)
        self.fields['contato'].widget.attrs['class'] = 'mask-contato'

