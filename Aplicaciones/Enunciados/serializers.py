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
            'carrera',
            'apellido1',
            'apellido2',
            'nombres',
            'correo',
            'edad',
            'sexo',
            'password',
            'anos_experiencia',
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
        
class UsuariosPasswordlessSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Usuarios
        fields = (
            'id',
            'rol',
            'carrera',
            'apellido1',
            'apellido2',
            'nombres',
            'correo',
            'edad',
            'sexo',
            'anos_experiencia',
            'date_joined','email','first_name','is_active','is_staff','is_superuser','last_login','last_name'
        )

class UsuariosPasswordSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Usuarios
        fields = (
            'id',
            'password'
            )

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
            'tipo',
            'respuesta',
            'active')

class DatosSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Datos
        fields = (
            'id',
            'enunciado',
            'usuario',
            'carrera',
            'rol',
            'edad',
            'sexo',
            'fecha_inicio',
            'fecha_termino',
            'solucion',
            'resultado',
            'nro_errores',
            'module_error',
            'name_error',
            'identation_error',
            'index_error',
            'syntax_error',
            'type_error',
            'value_error',
            'nro_lineas',
            'nro_ediciones',
            'nro_compilaciones',
            'nro_estrucflujo',
            'nro_operandos',
            'anos_experiencia',
            'respuesta')

class NasaSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Nasa
        fields = (
            'id',
            'enunciado',
            'data',
            'mental',
            'fisico',
            'tiempo',
            'performance',
            'esfuerzo',
            'frustracion',
            'result',)
