from functools import wraps
from atividades_funcionarios.models import Atividades
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

def dashboard_decorator(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        nao_resolvidos = Atividades.objects.filter(categoria='Nao Resolvido').count()
        em_andamento = Atividades.objects.filter(categoria='Em Progresso').count()
        finalizados = Atividades.objects.filter(categoria='Concluido').count()

        processos_por_mes = [0] * 12
        for atividade in Atividades.objects.all():
            mes = atividade.data_inicio.month - 1
            processos_por_mes[mes] += 1

        response = view_func(request, *args, **kwargs)

        if isinstance(response, dict):
            response.update({
                'nao_resolvidos': nao_resolvidos,
                'em_andamento': em_andamento,
                'finalizados': finalizados,
                'processos_por_mes': processos_por_mes,
            })
        elif hasattr(response, 'context_data'):
            response.context_data.update({
                'nao_resolvidos': nao_resolvidos,
                'em_andamento': em_andamento,
                'finalizados': finalizados,
                'processos_por_mes': processos_por_mes,
            })
        return response

    return wrapper

@login_required(login_url='/auth/login/')
@dashboard_decorator
def home_page(request):
    context = {}
    return render(request, 'index.html', context)