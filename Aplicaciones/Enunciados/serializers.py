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
            'carrera',
            'date_joined','email','first_name','is_active','is_staff','is_superuser','last_login','last_name'
        )
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create( self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
        



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
