from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('clientes/', views.clientes, name='clientes'),
    path('avaliacoes/', views.avaliacoes, name='avaliacoes'),
    path('dietas/', views.dietas, name='dietas'),
    path('retornos/', views.retornos, name='retornos'),
]
