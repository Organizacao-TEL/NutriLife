from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),

    path('clientes/', views.clientes, name='clientes'),
    path('clientes/cadastrar/', views.cadastrar_cliente, name='cadastrar_cliente'),
    path('clientes/editar/<int:id>/', views.editar_cliente, name='editar_cliente'),
    path('clientes/excluir/<int:id>/', views.excluir_cliente, name='excluir_cliente'),
    path('clientes/historico/<int:id>/', views.historico_cliente, name='historico_cliente'),

    path('avaliacoes/', views.avaliacoes, name='avaliacoes'),
    path('avaliacoes/cadastrar/', views.cadastrar_avaliacao, name='cadastrar_avaliacao'),
    path('avaliacoes/editar/<int:id>/', views.editar_avaliacao, name='editar_avaliacao'),
    path('avaliacoes/excluir/<int:id>/', views.excluir_avaliacao, name='excluir_avaliacao'),

    path('dietas/', views.dietas, name='dietas'),
    path('dietas/cadastrar/', views.cadastrar_dieta, name='cadastrar_dieta'),
    path('dietas/editar/<int:id>/', views.editar_dieta, name='editar_dieta'),
    path('dietas/excluir/<int:id>/', views.excluir_dieta, name='excluir_dieta'),

    path('retornos/', views.retornos, name='retornos'),
    path('retornos/cadastrar/', views.cadastrar_retorno, name='cadastrar_retorno'),
    path('retornos/editar/<int:id>/', views.editar_retorno, name='editar_retorno'),
    path('retornos/excluir/<int:id>/', views.excluir_retorno, name='excluir_retorno'),
]
