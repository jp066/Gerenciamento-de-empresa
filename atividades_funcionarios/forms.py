from django import forms
from .models import Atividades


class AtividadesForm(forms.ModelForm):
    class Meta:
        model = Atividades
        fields = ['nome', 'descricao', 'data_inicio', 'data_fim']
        widgets = {
            'data_inicio': forms.DateInput(attrs={'type': 'date'}),
            'data_fim': forms.DateInput(attrs={'type': 'date'}),
        }