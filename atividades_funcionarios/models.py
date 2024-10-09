from django.db import models

class Atividades(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    data_inicio = models.DateTimeField()
    data_fim = models.DateField()
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
    regiao = models.CharField(max_length=20, choices=REGIAO_CHOICES, default='Norte')
    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES, default='Nao Resolvido')

    def __str__(self):
        return self.nome