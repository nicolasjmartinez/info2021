from django.shortcuts import render
from django.contrib.auth.models import User


def inicio(request):
    template_name = 'inicio.html'  # template html a renderizar
    u = User.objects.get(username="nicoleto")
    u.last_name = 'Martínez'
    u.save()
    print(User.objects.all())
    ctx = {

    }
    return render(request, template_name, ctx)  # render tiene 3 parámetros


def login(request):
    template_name = 'login.html'  # template html a renderizar

    ctx = {

    }
    return render(request, template_name, ctx)  # render tiene 3 parámetros
