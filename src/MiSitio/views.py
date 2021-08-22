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


def login(request):
    template_name = 'login.html'  # template html a renderizar

    ctx = {

    }
    return render(request, template_name, ctx)  # render tiene 3 parámetros


def ini(request):
    template_name = 'ini.html'  # template html a renderizar

    ctx = {

    }
    return render(request, template_name, ctx)  # render tiene 3 parámetros
