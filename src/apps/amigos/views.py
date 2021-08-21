from django.shortcuts import render

from .models import Amigo


def listar_amigos(request):
    template_name = 'listar.html'  # template html a renderizar
    # El ctx (contexto es un diccionario)
    lista_de_amigos = Amigo.objects.all()  # ejecuta consulta en bd
    # lista_de_amigos = Amigo.objects.filter(id=1/top=1)
    # Los prints son para depurar errores
    print(lista_de_amigos.query)
    for a in lista_de_amigos:
        print(a)
    ctx = {
        'amigos': lista_de_amigos
    }
    return render(request, template_name, ctx)  # render tiene 3 parámetros
