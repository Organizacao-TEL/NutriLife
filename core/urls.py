from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),

    path('clientes/', views.clientes, name='clientes'),
    path('clientes/cadastrar/', views.cadastrar_cliente, name='cadastrar_cliente'),

    path('avaliacoes/', views.avaliacoes, name='avaliacoes'),
    path('dietas/', views.dietas, name='dietas'),
    path('retornos/', views.retornos, name='retornos'),
    path('clientes/editar/<int:id>/', views.editar_cliente, name='editar_cliente'),
    path('clientes/excluir/<int:id>/', views.excluir_cliente, name='excluir_cliente'),
]