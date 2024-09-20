from django.urls import path
from . import views

urlpatterns = [
    path('atividades/', views.lista_atividades, name='atividades-list'),
    path('criar-atividade/', views.criar_atividade, name='atividades-forms'),
    path('detalhes-atividades/<int:id>/', views.detalhes_atividade, name='atividades-detalhes'),
    path('update-atividades/<int:id>/', views.update_atividade, name='atividades-update'),
    path('delete-atividades/<int:id>/', views.atividade_delete, name='atividade-delete'),
]