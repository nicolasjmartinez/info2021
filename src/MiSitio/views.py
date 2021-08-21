from django.shortcuts import render


def inicio(request):
    template_name = 'inicio.html'  # template html a renderizar
    # El ctx (contexto es un diccionario)
    lista_alumnos = [
        'Alumno 1',
        'Alumno 2'
    ]
    ctx = {
        'username': 'nico',
        'lista': lista_alumnos

    }
    return render(request, template_name, ctx)  # render tiene 3 parámetros
