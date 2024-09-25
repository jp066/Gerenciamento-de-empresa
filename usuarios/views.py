from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse

def cadastro(request):
    if request.method == 'GET':
        return render(request, 'authSignup.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
    
        user = User.objects.filter(username=username).first()
        if user:
            return render(request, 'authSignin.html')
        

        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()
        return redirect('login')
        


def login(request):
    if request.method == 'GET':
        return render(request, 'authSignin.html')
    
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        
        user = authenticate(username=username, password=senha)
        
        # Se o usuário for autenticado, o usuário é logado e redirecionado para a página de autenticação
        if user:
            auth_login(request, user)
            return render(request, 'index.html', {'usuario': user.username})
        else:
            return render(request, 'loginErro.html', {'error': 'Usuário ou senha inválidos'})


def logout_view(request):
    logout(request)
    return redirect('authSignin.html') # Redireciona para a página de login


def listar_funcionarios(request):
    funcionarios = User.objects.all()  # Consulta todos os funcionários
    return render(request, 'funcionarios.html', {'funcionarios': funcionarios}) # passa o dict com os funcionários para o template