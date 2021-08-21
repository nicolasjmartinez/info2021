from django.db import models

# Create your models here.


class Amigo(models.Model):
    nombre = models.CharField(max_length=255)
    domicilio = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'amigos'

    # para que muestre el nombre
    def __str__(self):
        return self.nombre
