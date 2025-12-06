from django.db import models

#Crearemos un modelo basico (sin llave foranea)
class Rol(models.Model):
    nombre = models.TextField(max_length=100, unique=True)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

#Modelo con llave foranea
class User(models.Model):
    username = models.TextField(max_length=100, unique=True)
    password = models.TextField()
    foto = models.TextField()
    correo = models.TextField(unique=True)
    #llave foranea apunta a un modelo
    rol = models.ForeignKey(Rol, on_delete= models.CASCADE, related_name="users")

    def __str__(self):
        return f"{self.username} ({self.rol.nombre})"