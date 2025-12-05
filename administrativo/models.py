from django.db import models

#Crearemos un modelo basico (sin llave foranea)
class Rol(models.Model):
    nombre = models.TextField(max_length=100, unique=True)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


