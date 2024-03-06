from django.db import models

# Create your models here.
class Estudiantes (models.Model):
    nombre = models.CharField(max_length = 50) 
    apellido = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 50)
    edad = models.IntegerField(unique=True, null=True)

class Curso(models.Model):
    nombre = models.CharField(max_length=30)
    comision = models.IntegerField()

class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=40)

class Entregable(models.Model):
    nombre = models.CharField(max_length=30)
    fechaEntrega = models.DateField()
    entregado = models.BooleanField()
