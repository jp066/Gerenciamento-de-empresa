from django.shortcuts import get_object_or_404, render
from atividades_funcionarios.models import Atividades
from django.urls import reverse
from django.http import HttpResponseRedirect
from atividades_funcionarios.forms import AtividadesForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse # esse módulo é para retornar uma resposta em JSON, ou seja um objeto JSON

def lista_atividades(request):
    template_name = 'atividades-list.html'
    atividades = Atividades.objects.all()
    context = {
        'atividades': atividades
        } 
    return render(request, template_name, context)


def criar_atividade(request):
    if request.method == 'POST':
        form = AtividadesForm(request.POST) # o request.POST é para pegar os dados do formulário
        if form.is_valid():
            form = form.save(commit=False) # o commit=False é para não salvar no banco de dados ainda
            form.save() # Salva o objeto no banco de dados
            messages.success(request, 'Atividade cadastrada com sucesso!')
            return HttpResponseRedirect(reverse('atividades-list')) # o reverse é para redirecionar para a página de lista de atividades

    form = AtividadesForm()
    return render(request, 'atividades-forms.html', {'form': form})


def detalhes_atividade(request, id):
    template_name = 'atividades-detalhes.html'
    atividade = Atividades.objects.get(id=id)
    context = {
        'atividade': atividade
    }
    return render(request, template_name, context)


def update_atividade(request, id):
    atividade = get_object_or_404(Atividades, id=id)
    form = AtividadesForm(request.POST or None, instance=atividade)
    if form.is_valid():
        form.save()
        messages.success(request, 'Atividade atualizada com sucesso!')
        return HttpResponseRedirect(reverse('atividades-detalhes', args=[atividade.id]))
    return render(request, 'atividades-forms.html', {'form': form})


def atividade_delete(request, id):
    atividade = Atividades.objects.get(id=id) # Pega o objeto no banco de dados
    if request.method == 'POST':
        atividade.delete() # Deleta o objeto
        messages.success(request, 'Atividade deletada com sucesso!')
        return HttpResponseRedirect(reverse('atividades-list'))
    return render(request, 'atividades-delete.html', {'atividade': atividade})


@login_required(login_url='/auth/login/')
def func_page(request):
    return render(request, 'funcionarios.html')


def get_dados_atividades(request):
    atividades = Atividades.objects.all()
    dados = {
        'total': atividades.count(),
        'naoResolvidos': atividades.filter(status='naoResolvido').count(),
        'emAndamento': atividades.filter(status='emAndamento', deletado=False).count(),  # Considera atividades em andamento que não foram deletadas
        'finalizados': atividades.filter(deletado=True).count(),  # Considera atividades que foram deletadas
    }
    return JsonResponse(dados)