from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import json
from .models import CustomUser


def login_view(request):
    return render(request, 'login.html')


def cadastro_view(request):
    return render(request, 'cadastro.html')
