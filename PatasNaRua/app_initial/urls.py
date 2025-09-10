# app_initial/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Crie aqui os caminhos para as suas views
    path('', views.initial_page, name='initial_page'),
]
