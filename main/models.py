from django.db import models

# Create your models here.

class Mascota(models.Model):
    nombre = models.CharField(max_length=100)
    raza = models.CharField(max_length=100)
    descripcion = models.TextField()
    edad = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre


