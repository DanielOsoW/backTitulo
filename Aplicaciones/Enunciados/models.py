from django.db import models
#from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import AbstractUser
#from django.contrib.postgres.fields import ArrayField

# Create your models here.


class Roles(models.Model):
    nombre_rol = models.CharField(max_length=20)


class Carreras(models.Model):
    nombre_carrera = models.CharField(max_length=50)


class Usuarios(models.Model):
    rol = models.ForeignKey(Roles, to_field='id', on_delete=models.CASCADE)
    apellido1 = models.CharField(max_length=20)
    apellido2 = models.CharField(max_length=20)
    nombres = models.CharField(max_length=40)
    correo = models.CharField(max_length=40)
    password = models.CharField(max_length=255)
    carrera = models.ForeignKey(Carreras, to_field='id', on_delete=models.CASCADE, blank=True, null=True)

    REQUIRED_FIELDS = [correo]

class Enunciados(models.Model):
    titulo = models.CharField(max_length=50)
    enunciado = models.CharField(max_length=400)
    tipo = models.CharField(max_length=30)

    REQUIRED_FIELDS = [titulo,enunciado]

class Datos(models.Model):
    id_enunciado = models.ForeignKey(Enunciados, to_field='id', on_delete=models.CASCADE)
    id_estudiante = models.ForeignKey(Usuarios, to_field='id', on_delete=models.CASCADE)
    fecha_inicio = models.DateTimeField(auto_now_add=True, null=True, editable=False)
    fecha_termino = models.DateTimeField(auto_now_add=True, null=True)
    errores = models.IntegerField(null=True)

    REQUIRED_FIELDS = [id_estudiante,id_enunciado,fecha_inicio]
