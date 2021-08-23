from django.shortcuts import render


def login(request):
    template_name = 'login.html'  # template html a renderizar

    ctx = {

    }
    return render(request, template_name, ctx)  # render tiene 3 parámetros


def inicio(request):
    template_name = 'inicio.html'  # template html a renderizar

    ctx = {

    }
    return render(request, template_name, ctx)  # render tiene 3 parámetros
