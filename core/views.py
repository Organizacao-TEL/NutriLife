from django.shortcuts import render


def inicio(request):
    return render(request, 'core/inicio.html')


def clientes(request):
    return render(request, 'core/clientes.html')


def avaliacoes(request):
    return render(request, 'core/avaliacoes.html')


def dietas(request):
    return render(request, 'core/dietas.html')


def retornos(request):
    return render(request, 'core/retornos.html')
