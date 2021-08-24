from django.shortcuts import render
from django.contrib.auth.models import User

from django.contrib.auth import get_user_model
User = get_user_model()


def inicio(request):
    template_name = 'inicio.html'  # template html a renderizar
    u = User.objects.get(username="nicoleto")
    u.last_name = 'Martínez'
    u.save()
    print(User.objects.all())
    ctx = {

    }
    return render(request, template_name, ctx)  # render tiene 3 parámetros
