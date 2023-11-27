from django.conf import settings
from django.db import models

# Create your models here.

class Comentario(models.Model):
    nombre = models.CharField(max_length=200)
    correo = models.TextField()
    comentario = models.TextField()


    def __str__(self):
        return self.nombre

