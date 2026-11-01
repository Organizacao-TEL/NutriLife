from django.contrib import admin
from .models import Cliente, Avaliacao, Dieta, Retorno

admin.site.register(Cliente)
admin.site.register(Avaliacao)
admin.site.register(Dieta)
admin.site.register(Retorno)