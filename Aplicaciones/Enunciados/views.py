from django.shortcuts import render

from django.http import HttpResponse

from django.http.response import JsonResponse
from django.db.models import Count
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.contrib.auth.hashers import make_password

from . import models as models
from . import serializers as serials
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
import jwt, datetime
from django.core.mail import EmailMessage

# Create your views here.


def home(request):
    return HttpResponse('<h1>Home</h1>')


def about(request):
    return HttpResponse('<h1>About</h1>')

# CRUD roles

@api_view(['GET', 'DELETE'])
def lista_roles(request):
    if request.method == 'GET':
        roles = models.Roles.objects.all()

        '''
        El tutorial incluye una forma de filtrar resultados. Dejo el codigo comentado por si
        es de utilidad para el futuro. El ejemplo original eran titulos de posts.
        
        nombre_rol = request.GET.get('nombre_rol', None)
        if nombre_rol is not NONE:
            roles = roles.filter(nombre_rol__icontains=nombre_rol)
        '''

        rolesSerializer = serials.RolesSerializer(roles, many=True)
        return JsonResponse(rolesSerializer.data, safe=False)

    elif request.method == 'DELETE':
        count = models.Roles.objects.all().delete()
        return JsonResponse({'message': 'Se borraron exitosamente {} roles.'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def crear_rol(request):
    rolData = JSONParser().parse(request)
    rolesSerializer = serials.RolesSerializer(data=rolData)
    if rolesSerializer.is_valid():
        rolesSerializer.save()
        return JsonResponse(rolesSerializer.data, status=status.HTTP_201_CREATED)
    else:
        return JsonResponse(rolesSerializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def encontrar_rol(request, pk):
    rol = models.Roles.objects.get(pk=pk)

    if request.method == 'GET':
        rolesSerializer = serials.RolesSerializer(rol)
        return JsonResponse(rolesSerializer.data)

    elif request.method in ['PUT', 'PATCH']:
        rolData = JSONParser().parse(request)
        rolesSerializer = serials.RolesSerializer(rol, data=rolData)
        if rolesSerializer.is_valid():
            rolesSerializer.save()
            return JsonResponse(rolesSerializer.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(rolesSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        rol.delete()
        return JsonResponse({'message': 'El rol fue correctamente eliminado'}, status=status.HTTP_204_NO_CONTENT)


# CRUD Usuarios

@api_view(['GET', 'DELETE'])
def lista_usuarios(request):
    if request.method == 'GET':
        usuarios = models.Usuarios.objects.all()
        usuariosSerializer = serials.UsuariosSerializer(usuarios, many=True)
        return JsonResponse(usuariosSerializer.data, safe=False)

    elif request.method == 'DELETE':
        count = models.Usuarios.objects.all().delete()
        return JsonResponse({'message': 'Se borraron exitosamente {} usuarios.'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def lista_alumnos(request):
    alumnos = models.Usuarios.objects.filter(rol="1")
    usuariosSerializer = serials.UsuariosSerializer(alumnos, many=True)
    return JsonResponse(usuariosSerializer.data, safe=False)



@api_view(['POST'])
def lista_alumnos_rut(request):
    run = JSONParser().parse(request)['run']
    alumnos = models.Usuarios.objects.get(run=run)
    usuariosSerializer = serials.UsuariosSerializer(alumnos)
    return JsonResponse(usuariosSerializer.data, safe=False)





@api_view(['POST'])
def crear_usuario(request):
    usuarioData = JSONParser().parse(request)
    usuariosSerializer = serials.UsuariosSerializer(data=usuarioData)
    if usuariosSerializer.is_valid():
        usuariosSerializer.save()
        return JsonResponse(usuariosSerializer.data, status=status.HTTP_201_CREATED)
    else:
        return JsonResponse(usuariosSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def encontrar_usuario(request, pk):
    usuario = models.Usuarios.objects.get(pk=pk)

    if request.method == 'GET':
        usuariosSerializer = serials.UsuariosSerializer(usuario)
        return JsonResponse(usuariosSerializer.data)

    elif request.method in ['PUT', 'PATCH']:
        usuarioData = JSONParser().parse(request)
        usuariosSerializer = serials.UsuariosSerializer(usuario, data=usuarioData)
        if usuariosSerializer.is_valid():
            usuariosSerializer.save()
            return JsonResponse(usuariosSerializer.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(usuariosSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        usuario.delete()
        return JsonResponse({'message': 'El usuario fue correctamente eliminado'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def encontrar_usuario_passwordless(request, pk):
    usuario = models.Usuarios.objects.get(pk=pk)

    if request.method == 'GET':
        usuariosSerializer = serials.UsuariosPasswordlessSerializer(usuario)
        return JsonResponse(usuariosSerializer.data)

    elif request.method in ['PUT', 'PATCH']:
        usuarioData = JSONParser().parse(request)
        usuariosSerializer = serials.UsuariosPasswordlessSerializer(usuario, data=usuarioData)
        if usuariosSerializer.is_valid():
            usuariosSerializer.save()
            return JsonResponse(usuariosSerializer.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(usuariosSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        usuario.delete()
        return JsonResponse({'message': 'El usuario fue correctamente eliminado'}, status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def encontrar_usuario_just_pwd(request, pk):
    usuario = models.Usuarios.objects.get(pk=pk)

    if request.method == 'GET':
        usuariosSerializer = serials.UsuariosPasswordSerializer(usuario)
        return JsonResponse(usuariosSerializer.data)

    elif request.method in ['PUT', 'PATCH']:
        usuarioData = JSONParser().parse(request)
        pwd = usuarioData['old_password']
        check = usuario.check_password(pwd)
        
        usuarioData['password'] = make_password(usuarioData['password'])
        usuariosSerializer = serials.UsuariosPasswordSerializer(usuario, data=usuarioData)

        if not check:
            return JsonResponse({'message': 'La clave actual ingresada no coincide.'},
                status=status.HTTP_201_CREATED)

        if usuariosSerializer.is_valid():
            usuariosSerializer.save()
            return JsonResponse({'message': 'La clave se ha modificado con exito.'}, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(usuariosSerializer.errors, status=status.HTTP_400_BAD_REQUEST)




# CRUD Carreras

@api_view(['GET', 'DELETE'])
def lista_carreras(request):
    if request.method == 'GET':
        carreras = models.Carreras.objects.all()
        carrerasSerializer = serials.CarrerasSerializer(carreras, many=True)
        return JsonResponse(carrerasSerializer.data, safe=False)

    elif request.method == 'DELETE':
        count = models.Carreras.objects.all().delete()
        return JsonResponse({'message': 'Se borraron exitosamente {} carreras.'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def crear_carrera(request):
    carreraData = JSONParser().parse(request)
    carrerasSerializer = serials.CarrerasSerializer(data=carreraData)
    if carrerasSerializer.is_valid():
        carrerasSerializer.save()
        return JsonResponse(carrerasSerializer.data, status=status.HTTP_201_CREATED)
    else:
        return JsonResponse(carrerasSerializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def encontrar_carrera(request, pk):
    carrera = models.Carreras.objects.get(pk=pk)

    if request.method == 'GET':
        carrerasSerializer = serials.CarrerasSerializer(carrera)
        return JsonResponse(carrerasSerializer.data)

    elif request.method in ['PUT', 'PATCH']:
        carreraData = JSONParser().parse(request)
        carrerasSerializer = serials.CarrerasSerializer(carrera, data=carreraData)
        if carrerasSerializer.is_valid():
            carrerasSerializer.save()
            return JsonResponse(carrerasSerializer.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(carrerasSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        carrera.delete()
        return JsonResponse({'message': 'La carrera fue correctamente eliminada'}, status=status.HTTP_204_NO_CONTENT)

# CRUD Enunciados

@api_view(['GET', 'DELETE'])
def lista_enunciados(request):
    if request.method == 'GET':
        enunciados = models.Enunciados.objects.all()
        enunciadosSerializer = serials.EnunciadosSerializer(enunciados, many=True)
        return JsonResponse(enunciadosSerializer.data, safe=False)

    elif request.method == 'DELETE':
        count = models.Enunciados.objects.all().delete()
        return JsonResponse({'message': 'Se borraron exitosamente {} enunciados.'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def crear_enunciado(request):
    enunciadoData = JSONParser().parse(request)
    enunciadosSerializer = serials.EnunciadosSerializer(data=enunciadoData)
    if enunciadosSerializer.is_valid():
        enunciadosSerializer.save()
        return JsonResponse(enunciadosSerializer.data, status=status.HTTP_201_CREATED)
    else:
        return JsonResponse(enunciadosSerializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def encontrar_enunciado(request, pk):
    enunciado = models.Enunciados.objects.get(pk=pk)

    if request.method == 'GET':
        enunciadosSerializer = serials.EnunciadosSerializer(enunciado)
        return JsonResponse(enunciadosSerializer.data)

    elif request.method in ['PUT', 'PATCH']:
        enunciadoData = JSONParser().parse(request)
        enunciadosSerializer = serials.EnunciadosSerializer(enunciado, data=enunciadoData)
        if enunciadosSerializer.is_valid():
            enunciadosSerializer.save()
            return JsonResponse(enunciadosSerializer.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(enunciadosSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        enunciado.delete()
        return JsonResponse({'message': 'El enunciado fue correctamente eliminado'}, status=status.HTTP_204_NO_CONTENT)

# CRUD Datos

@api_view(['GET', 'DELETE'])
def lista_datos(request):
    if request.method == 'GET':
        datos = models.Datos.objects.all()
        datosSerializer = serials.DatosSerializer(datos, many=True)
        return JsonResponse(datosSerializer.data, safe=False)

    elif request.method == 'DELETE':
        count = models.Datos.objects.all().delete()
        return JsonResponse({'message': 'Se borraron exitosamente {} datos.'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def crear_datos(request):
    datosData = JSONParser().parse(request)
    datosSerializer = serials.DatosSerializer(data=datosData)
    if datosSerializer.is_valid():
        datosSerializer.save()
        return JsonResponse(datosSerializer.data, status=status.HTTP_201_CREATED)
    else:
        return JsonResponse(datosSerializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def encontrar_datos(request, pk):
    dato = models.Datos.objects.get(pk=pk)

    if request.method == 'GET':
        datosSerializer = serials.DatosSerializer(dato)
        return JsonResponse(datosSerializer.data)

    elif request.method in ['PUT', 'PATCH']:
        datoData = JSONParser().parse(request)
        datosSerializer = serials.DatosSerializer(dato, data=datoData)
        if datosSerializer.is_valid():
            datosSerializer.save()
            return JsonResponse(datosSerializer.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(datosSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        dato.delete()
        return JsonResponse({'message': 'El dato fue correctamente eliminado'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def encontrar_datos_cruz(request, pk):
    datos_cruz = models.Datos.objects.filter(id_enunciado=pk,fecha_termino__isnull=False)
    datos_cruzSerializer = serials.DatosSerializer(datos_cruz, many=True)
    return JsonResponse(datos_cruzSerializer.data, safe=False)

# Login

@api_view(['POST'])
def encontrar_user(request):
    tok = JSONParser().parse(request)
    token = tok['jwt']
    if not token:
        response.data = {
        'message': 'success'
    }

    try:
        payload = jwt.decode(token, 'secret', algorithms='HS256')
    except jwt.ExpiredSignatureError:
        response.data = {
        'message': 'success'
    }


    user = models.Usuarios.objects.get(id=payload['id'])
    serializer = serials.UsuariosSerializer(user)


    return Response(serializer.data)
   
@api_view(['POST'])
def login_user(request):
    tok = JSONParser().parse(request)
    correo = tok['correo']
    password = tok['password']

    user = models.Usuarios.objects.filter(correo=correo).first()
    if user is None:
        return JsonResponse({'message':'No existe'}, status=status.HTTP_400_BAD_REQUEST)
    if not user.check_password(password):
        return JsonResponse({'message':'Mala contra'}, status=status.HTTP_400_BAD_REQUEST)
    payload = {
        'id': user.id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
        'iat': datetime.datetime.utcnow()
    }

    token = jwt.encode(payload, 'secret', algorithm='HS256')

    response = Response()
    
    response.data ={
        'jwt': token
    }
    return response



class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response

# CRUD Nasa

@api_view(['GET', 'DELETE'])
def lista_nasa(request):
    if request.method == 'GET':
        nasa = models.Nasa.objects.all()
        nasaSerializer = serials.NasaSerializer(nasa, many=True)
        return JsonResponse(nasaSerializer.data, safe=False)

    elif request.method == 'DELETE':
        count = models.Nasa.objects.all().delete()
        return JsonResponse({'message': 'Se borraron exitosamente {} datos.'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def crear_nasa(request):
    nasaData = JSONParser().parse(request)
    nasaSerializer = serials.NasaSerializer(data=nasaData)
    if nasaSerializer.is_valid():
        nasaSerializer.save()
        return JsonResponse(nasaSerializer.data, status=status.HTTP_201_CREATED)
    else:
        return JsonResponse(nasaSerializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def encontrar_nasa(request, pk):
    nasa = models.Nasa.objects.get(pk=pk)

    if request.method == 'GET':
        nasaSerializer = serials.NasaSerializer(nasa)
        return JsonResponse(nasaSerializer.data)

    elif request.method in ['PUT', 'PATCH']:
        nasaData = JSONParser().parse(request)
        nasaSerializer = serials.NasaSerializer(nasa, data=nasaData)
        if nasaSerializer.is_valid():
            nasaSerializer.save()
            return JsonResponse(nasaSerializer.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(nasaSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        nasa.delete()
        return JsonResponse({'message': 'El dato fue correctamente eliminado'}, status=status.HTTP_204_NO_CONTENT)
