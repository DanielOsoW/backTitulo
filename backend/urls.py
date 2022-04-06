"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Aplicaciones.Enunciados import views as views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='backend-home'),
    path('about/', views.about, name='backend-about'),

    # CRUD roles
    path('roles/all', views.lista_roles),  # Obtener o eliminar todos los roles
    path('roles/create', views.crear_rol),  # Crear nuevo rol
    path('roles/<int:pk>', views.encontrar_rol),  # Leer, actualizar o eliminar un rol.

    # CRUD usuarios
    path('usuarios/all', views.lista_usuarios),  # Obtener o eliminar todos los usuarios
    path('alumnos/all', views.lista_alumnos),  # Obtener todos los alumnos
    path('alumno_rut', views.lista_alumnos_rut),  # Obtener al usuario segun su rut
    path('usuarios/create', views.crear_usuario),  # Crear nuevo usuario
    path('usuarios/<int:pk>', views.encontrar_usuario),  # Leer, actualizar o eliminar un usuario
    path('usuarios/passwordless/<int:pk>', views.encontrar_usuario_passwordless),  # Leer, actualizar o eliminar un usuario sin contraseña
    path('editUsuarios/<int:pk>', views.encontrar_usuario),  # Leer, actualizar o eliminar un rol (duplicada)
    path('usuarios/changePassword/<int:pk>', views.encontrar_usuario_just_pwd),

    # CRUD carreras
    path('carreras/all', views.lista_carreras),  # Obtener o eliminar todas las carreras
    path('carreras/create', views.crear_carrera),  # Crear nueva carrera
    path('carreras/<int:pk>', views.encontrar_carrera),  # Leer, actualizar o eliminar una carrera

    # CRUD enunciados
    path('enunciados/all', views.lista_enunciados),  # Obtener o eliminar todas las carreras
    path('enunciados/create', views.crear_enunciado),  # Crear nueva carrera
    path('enunciados/<int:pk>', views.encontrar_enunciado),  # Leer, actualizar o eliminar una carrera

    # CRUD datos
    path('datos/all', views.lista_datos),  # Obtener o eliminar todas las carreras
    path('datos/create', views.crear_datos),  # Crear nueva carrera
    path('datos/<int:pk>', views.encontrar_datos),  # Leer, actualizar o eliminar una carrera
]
