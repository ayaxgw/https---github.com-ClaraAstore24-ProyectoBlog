from django.db import models

# Create your models here.

class Usuario(models.Model):
    contraseña = models.CharField(max_length=50)
    email = models.EmailField()

class Registrar(models.Model):
    nombre = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=50)
    email = models.EmailField()

class Publicaciones(models.Model):
    titulo = models.CharField(max_length=20)
    comentarios = models.CharField(max_length=280)
    