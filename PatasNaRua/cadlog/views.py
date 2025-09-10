from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import json
from .models import CustomUser


def home_view(request):
    """Página inicial - redireciona conforme o status do usuário"""
    if request.user.is_authenticated:
        return redirect('dashboard')
    return redirect('login')

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if not email or not password:
            messages.error(request, 'Email e senha são obrigatórios')
            return render(request, 'cadlog/login.html')
        
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'Login realizado com sucesso!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Email ou senha incorretos')
    
    return render(request, 'cadlog/login.html')

def cadastro_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        telefone = request.POST.get('telefone', '')
        
        errors = []
        
        if not username or not email or not password:
            errors.append('Todos os campos obrigatórios devem ser preenchidos')
        
        if password != confirm_password:
            errors.append('As senhas não coincidem')
        
        if len(password) < 8:
            errors.append('A senha deve ter pelo menos 8 caracteres')
        
        if CustomUser.objects.filter(email=email).exists():
            errors.append('Este email já está cadastrado')
        
        if CustomUser.objects.filter(username=username).exists():
            errors.append('Este nome de usuário já está em uso')
        
        if errors:
            for error in errors:
                messages.error(request, error)
            return render(request, 'cadastro.html')
        
        try:
            user = CustomUser.objects.create_user(
                username=username,
                email=email,
                password=password,
                telefone=telefone
            )
            
            messages.success(request, 'Cadastro realizado com sucesso! Faça login para continuar.')
            return redirect('login')
            
        except Exception as e:
            messages.error(request, f'Erro ao criar usuário: {str(e)}')
    
    return render(request, 'cadastro.html')

@login_required
def dashboard_view(request):
    return render(request, 'dashboard.html', {'user': request.user})

def logout_view(request):
    logout(request)
    messages.success(request, 'Logout realizado com sucesso!')
    return redirect('login')