from django.db import models

# Create your models here.
class Login(models.Model):
    #REGISTRARSE
    usuario = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    Telefono = models.IntegerField()
    contraseña = models.CharField(max_length=50)
    contraseñaCON = models.CharField(max_length=50)
class Cursos(models.Model):
    #REGISTRARSE
    usuario = models.CharField(max_length=50)


