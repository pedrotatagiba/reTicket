# reTicket/ingressos/forms.py
from django import forms
from ingressos.models import Evento

class IngressoModel2Form(forms.ModelForm):
    dtEvento = forms.DateField(
    	input_formats=['%d/%m/%Y'],
    	label='Data do evento',
    	help_text='Data no formato DD/MM/AAAA',
        )
    class Meta:
        model = Evento
        # Remova 'user' dos fields, ele será preenchido na view
        fields = ['nome', 'codigo', 'dtEvento', 'preco']
        # Ou, se preferir usar '__all__' e excluir, pode ser assim:
        # exclude = ['user']