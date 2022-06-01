from django.db import models
#from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import AbstractUser
#from django.contrib.postgres.fields import ArrayField

# Create your models here.


class Roles(models.Model):
    nombre_rol = models.CharField(max_length=20)


class Carreras(models.Model):
    nombre_carrera = models.CharField(max_length=50)


class Usuarios(AbstractUser):
    rol = models.ForeignKey(Roles, to_field='id', on_delete=models.CASCADE)
    apellido1 = models.CharField(max_length=20)
    apellido2 = models.CharField(max_length=20)
    nombres = models.CharField(max_length=40)
    correo = models.CharField(max_length=40, unique=True)
    edad = models.IntegerField(null=True)
    sexo = models.CharField(max_length=40,null=True)
    password = models.CharField(max_length=255)
    carrera = models.ForeignKey(Carreras, to_field='id', on_delete=models.CASCADE, blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True, null=True)
    email = models.CharField(max_length=40, null = True)
    first_name = models.CharField(max_length=20, null = True)
    is_active = models.BooleanField(default=False, null = True)
    is_staff = models.BooleanField(default=False, null = True)
    is_superuser = models.BooleanField(default=False, null = True)
    last_login = models.DateTimeField(auto_now_add=True, null=True)
    last_name = models.DateTimeField(auto_now_add=True, null=True)
    username = None
    

    USERNAME_FIELD = 'correo'
    REQUIRED_FIELDS = []

class Enunciados(models.Model):
    titulo = models.CharField(max_length=50)
    enunciado = models.CharField(max_length=400)
    tipo = models.CharField(max_length=30)

    REQUIRED_FIELDS = [titulo,enunciado]

class Datos(models.Model):
    id_enunciado = models.ForeignKey(Enunciados, to_field='id', on_delete=models.CASCADE)
    id_estudiante = models.ForeignKey(Usuarios, to_field='id', on_delete=models.CASCADE, null=True)
    edad = models.IntegerField(null=True)
    sexo = models.CharField(max_length=40,null=True)
    fecha_inicio = models.DateTimeField(auto_now_add=True, null=True, editable=False)
    fecha_termino = models.DateTimeField(null=True)
    solucion = models.CharField(max_length=400,null=True, blank=True)
    resultado = models.CharField(max_length=400,null=True, blank=True)
    nro_errores = models.IntegerField(null=True)
    module_error = models.IntegerField(null=True)
    name_error = models.IntegerField(null=True)
    identation_error = models.IntegerField(null=True)
    index_error = models.IntegerField(null=True)
    syntax_error = models.IntegerField(null=True)
    type_error = models.IntegerField(null=True)
    value_error = models.IntegerField(null=True)
    nro_lineas = models.IntegerField(null=True)
    nro_ediciones = models.IntegerField(null=True)
    nro_compilaciones = models.IntegerField(null=True)

    REQUIRED_FIELDS = [id_enunciado,fecha_inicio]

class Nasa(models.Model):
    id_enunciado = models.ForeignKey(Enunciados, to_field='id', on_delete=models.CASCADE)
    id_data = models.ForeignKey(Datos, to_field='id', on_delete=models.CASCADE)
    mental = models.IntegerField(null=True)
    fisico = models.IntegerField(null=True)
    tiempo = models.IntegerField(null=True)
    performance = models.IntegerField(null=True)
    esfuerzo = models.IntegerField(null=True)
    frustracion = models.IntegerField(null=True)
    result = models.IntegerField(null=True)

    REQUIRED_FIELDS = [id_enunciado,id_data]