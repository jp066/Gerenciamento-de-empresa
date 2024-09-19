from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required

def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
    
        user = User.objects.filter(username=username).first()
        
        if user:
            return HttpResponse('Usuário já cadastrado')
        

        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()

        return HttpResponse(f'Usuário: {username}')


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        
        user = authenticate(username=username, password=senha)
        
        if user:
            auth_login(request, user)
            return HttpResponse('Logado')
        else:
            return HttpResponse('Usuário ou senha inválidos')


@login_required(login_url='/auth/login/')
def home(request):
        return render(request, 'home.html')