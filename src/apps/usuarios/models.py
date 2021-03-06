from django.db import models
from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):
    apodo = models.CharField(max_length=255, null=True, blank=True)
    fecha_nacimieto = models.DateField(null=True, blank=True)
    direccion = models.CharField(max_length=255, null=True, blank=True)
    telefono = models.CharField(max_length=255, null=True, blank=True)

    class Meta:  # Renombra tabla
        db_table = 'usuarios'
