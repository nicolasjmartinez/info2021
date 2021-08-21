from django.urls import path

from .import views

app_name = 'amigos'

urlpatterns = [
    path('listar/', views.listar_amigos)  # Cuando escribo listar/ llama a :
]
