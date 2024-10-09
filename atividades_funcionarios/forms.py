from django import forms
from .models import Atividades


class AtividadesForm(forms.ModelForm):
    REGIAO_CHOICES = [
        ('Norte', 'Norte'),
        ('Nordeste', 'Nordeste'),
        ('Centro-Oeste', 'Centro-Oeste'),
        ('Sudeste', 'Sudeste'),
        ('Sul', 'Sul'),
    ]

    CATEGORIA_CHOICES = [
        ('Nao Resolvido', 'Não Resolvido'),
        ('Em Progresso', 'Em Progresso'),
        ('Concluido', 'Concluído'),
    ]

    regiao = forms.ChoiceField(choices=REGIAO_CHOICES)
    categoria = forms.ChoiceField(choices=CATEGORIA_CHOICES)

    class Meta:
        model = Atividades
        fields = ['nome', 'descricao', 'data_inicio', 'data_fim', 'regiao', 'categoria']
        widgets = {
            'data_inicio': forms.DateInput(attrs={'type': 'date'}),
            'data_fim': forms.DateInput(attrs={'type': 'date'}),
        }
