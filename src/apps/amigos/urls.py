from django.urls import path

from .import views

app_name = 'amigos'

urlpatterns = [
    # Cuando escribo listar/ llama a :
    path('listar/', views.listar_amigos, name='listar')
]
