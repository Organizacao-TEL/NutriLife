from django.shortcuts import render, redirect
from .models import Cliente
from .forms import ClienteForm


def inicio(request):
    return render(request, 'core/inicio.html')


def clientes(request):
    busca = request.GET.get('busca')

    if busca:
        lista_clientes = Cliente.objects.filter(nome__icontains=busca)
    else:
        lista_clientes = Cliente.objects.all()

    return render(request, 'core/clientes.html', {
        'clientes': lista_clientes
    })


def cadastrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('clientes')
    else:
        form = ClienteForm()

    return render(request, 'core/form_cliente.html', {
        'form': form
    })

def editar_cliente(request, id):
    cliente = Cliente.objects.get(id=id)

    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)

        if form.is_valid():
            form.save()
            return redirect('clientes')
    else:
        form = ClienteForm(instance=cliente)

    return render(request, 'core/form_cliente.html', {
        'form': form
    })

def avaliacoes(request):
    return render(request, 'core/avaliacoes.html')


def dietas(request):
    return render(request, 'core/dietas.html')


def retornos(request):
    return render(request, 'core/retornos.html')

def excluir_cliente(request, id):
    cliente = Cliente.objects.get(id=id)

    if request.method == 'POST':
        cliente.delete()
        return redirect('clientes')

    return render(request, 'core/excluir_cliente.html', {
        'cliente': cliente
    })