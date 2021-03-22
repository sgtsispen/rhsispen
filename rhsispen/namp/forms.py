from django import forms

class ServidorFormAdmin(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ServidorFormAdmin, self).__init__(*args, **kwargs)
        self.fields['cpf'].widget.attrs={"placeholder":"000.000.000-00"} #Aparece no campo digitavel do usuario
        self.fields['cpf'].widget.attrs['class'] = 'mask-cpf'
        self.fields['dt_nasc'].widget.attrs={"placeholder":"00/00/0000"}
        self.fields['dt_nasc'].widget.attrs['class'] = 'mask-dt_nasc'
 
class EnderecoFormAdmin(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EnderecoFormAdmin, self).__init__(*args, **kwargs)
        self.fields['cep'].widget.attrs={"placeholder":"00000-000"}       
        self.fields['cep'].widget.attrs['class'] = 'mask-cep'

class ContatoFormAdmin(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ContatoFormAdmin, self).__init__(*args, **kwargs)
        self.fields['contato'].widget.attrs['class'] = 'mask-contato'

class TextFormAdmin(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TextFormAdmin, self).__init__(*args, **kwargs)
        self.fields['descricao'].widget.attrs={"placeholder":
                                               "Digite com detalhamento",
                                               "rows": 15,
                                               "cols": 50}

#widgets = {'cpf': forms.TextInput(attrs={'cpf-mask':"000.000.000-00"})}
'''
from input_mask.widgets import InputMask


class MyCustomInput(InputMask):
   mask = {'cpf': '000.000.000-00'}'''