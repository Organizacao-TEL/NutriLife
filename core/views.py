from django.shortcuts import render, redirect
from .models import Cliente, Avaliacao, Dieta, Retorno
from .forms import ClienteForm, AvaliacaoForm, DietaForm, RetornoForm

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
    lista_avaliacoes = Avaliacao.objects.all()

    return render(request, 'core/avaliacoes.html', {
        'avaliacoes': lista_avaliacoes
    })

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

def cadastrar_avaliacao(request):
    if request.method == 'POST':
        form = AvaliacaoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('avaliacoes')
    else:
        form = AvaliacaoForm()

    return render(request, 'core/form_avaliacao.html', {
        'form': form
    })

def editar_avaliacao(request, id):
    avaliacao = Avaliacao.objects.get(id=id)

    if request.method == 'POST':
        form = AvaliacaoForm(request.POST, instance=avaliacao)

        if form.is_valid():
            form.save()
            return redirect('avaliacoes')
    else:
        form = AvaliacaoForm(instance=avaliacao)

    return render(request, 'core/form_avaliacao.html', {
        'form': form
    })

def excluir_avaliacao(request, id):
    avaliacao = Avaliacao.objects.get(id=id)

    if request.method == 'POST':
        avaliacao.delete()
        return redirect('avaliacoes')

    return render(request, 'core/excluir_avaliacao.html', {
        'avaliacao': avaliacao
    })
def dietas(request):
    lista_dietas = Dieta.objects.all()
    return render(request, 'core/dietas.html', {'dietas': lista_dietas})


def cadastrar_dieta(request):
    if request.method == 'POST':
        form = DietaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dietas')
    else:
        form = DietaForm()

    return render(request, 'core/form_dieta.html', {'form': form})


def editar_dieta(request, id):
    dieta = Dieta.objects.get(id=id)

    if request.method == 'POST':
        form = DietaForm(request.POST, instance=dieta)
        if form.is_valid():
            form.save()
            return redirect('dietas')
    else:
        form = DietaForm(instance=dieta)

    return render(request, 'core/form_dieta.html', {'form': form})


def excluir_dieta(request, id):
    dieta = Dieta.objects.get(id=id)

    if request.method == 'POST':
        dieta.delete()
        return redirect('dietas')

    return render(request, 'core/excluir_dieta.html', {'dieta': dieta})
def historico_cliente(request, id):
    cliente = Cliente.objects.get(id=id)

    avaliacoes = cliente.avaliacao_set.all()
    dietas = cliente.dieta_set.all()
    retornos = cliente.retorno_set.all()

    return render(request, 'core/historico.html', {
        'cliente': cliente,
        'avaliacoes': avaliacoes,
        'dietas': dietas,
        'retornos': retornos
    })
def retornos(request):
    lista_retornos = Retorno.objects.all()
    return render(request, 'core/retornos.html', {'retornos': lista_retornos})


def cadastrar_retorno(request):
    if request.method == 'POST':
        form = RetornoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('retornos')
    else:
        form = RetornoForm()

    return render(request, 'core/form_retorno.html', {'form': form})


def editar_retorno(request, id):
    retorno = Retorno.objects.get(id=id)

    if request.method == 'POST':
        form = RetornoForm(request.POST, instance=retorno)
        if form.is_valid():
            form.save()
            return redirect('retornos')
    else:
        form = RetornoForm(instance=retorno)

    return render(request, 'core/form_retorno.html', {'form': form})


def excluir_retorno(request, id):
    retorno = Retorno.objects.get(id=id)

    if request.method == 'POST':
        retorno.delete()
        return redirect('retornos')

    return render(request, 'core/excluir_retorno.html', {'retorno': retorno})
