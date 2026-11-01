from django.db import models

# Create your models here.


from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.PositiveIntegerField()
    peso = models.FloatField()
    altura = models.FloatField()
    contato = models.CharField(max_length=20)

    def __str__(self):
        return self.nome


class Avaliacao(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data = models.DateField(auto_now_add=True)
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    altura = models.FloatField()
    cintura = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    quadril = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    observacoes = models.TextField(blank=True)

    def __str__(self):
        return self.cliente.nome


class Dieta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    data_cadastro = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nome


class Retorno(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data = models.DateField(auto_now_add=True)
    evolucao = models.TextField()
    ajustes = models.TextField(blank=True)
    observacoes = models.TextField(blank=True)

    def __str__(self):
        return self.cliente.nome
