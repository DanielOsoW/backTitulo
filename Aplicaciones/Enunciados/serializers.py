from rest_framework import serializers
from . import models as models

class RolesSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Roles
        fields = (
            'id',
            'nombre_rol')

class CarrerasSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Carreras
        fields = (
            'id',
            'nombre_carrera')


class UsuariosSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Usuarios
        fields = (
            'id',
            'rol',
            'apellido1',
            'apellido2',
            'nombres',
            'correo',
            'password',
            'carrera'
        )
        #extra_kwargs = {
        #    'password': {'write_only': True}
        #}



class EnunciadosSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Enunciados
        fields = (
            'id',
            'titulo',
            'enunciado',
            'tipo')

class DatosSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Datos
        fields = (
            'id',
            'id_enunciados',
            'id_estudiante',
            'fecha_inicio',
            'fecha_termino',
            'errores')
