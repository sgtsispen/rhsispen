from django import forms

class ServidorFormAdmin(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ServidorFormAdmin, self).__init__(*args, **kwargs)
        self.fields['cpf'].widget.attrs={"placeholder":"000.000.000-00"} #Aparece no campo digitavel do usuario
        self.fields['cpf'].widget.attrs['class'] = 'mask-cpf'
        self.fields['dt_nasc'].widget.attrs={"placeholder":"00/00/0000"}
        self.fields['dt_nasc'].widget.attrs['class'] = 'mask-dt'
 
class EnderecoFormAdmin(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EnderecoFormAdmin, self).__init__(*args, **kwargs)
        self.fields['cep'].widget.attrs={"placeholder":"00000-000"}       
        self.fields['cep'].widget.attrs['class'] = 'mask-cep'

class TextFormAdmin(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TextFormAdmin, self).__init__(*args, **kwargs)
        self.fields['descricao'].widget.attrs={"placeholder":
                                               "Digite com detalhamento",
                                               "rows": 15,
                                               "cols": 50}

class HoraFormAdmin(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(HoraFormAdmin, self).__init__(*args, **kwargs)
        self.fields['hora_inicial'].widget.attrs={"placeholder":"00:00"} 
        self.fields['hora_inicial'].widget.attrs['class'] = 'mask-hr'

class HistStatusFuncionalFormAdmin(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(HistStatusFuncionalFormAdmin, self).__init__(*args, **kwargs)
        self.fields['data_inicial'].widget.attrs={"placeholder":"00/00/0000"}
        self.fields['data_inicial'].widget.attrs['class'] = 'mask-data'
        self.fields['data_final'].widget.attrs = {"placeholder":"00/00/0000"}
        self.fields['data_final'].widget.attrs['class'] = 'mask-data'