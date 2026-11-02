from django import forms
from .models import Cliente, Avaliacao, Dieta


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'idade', 'peso', 'altura', 'contato']


class AvaliacaoForm(forms.ModelForm):
    class Meta:
        model = Avaliacao
        fields = ['cliente', 'peso', 'altura', 'cintura', 'quadril', 'observacoes']


class DietaForm(forms.ModelForm):
    class Meta:
        model = Dieta
        fields = ['cliente', 'nome', 'descricao']