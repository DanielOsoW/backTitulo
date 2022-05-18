backTitulo

# Descripción

Backend para la plataforma de administración y seguimiento del departamento de ingenierías multidisciplinarias de la Universidad de Santiago de Chile. 

# Requisitos

Se requiere haber instalado Python 3 en la máquina a utilizar. Python 3.9 presenta actualmente incompatibilidades, por lo que se requiere una versión previa.

https://www.python.org/downloads/

Se requiere también tener instalado el motor de base de datos PostgreSQL versión 13 o superior, y haber creado una base de datos 
(vacía) para el uso del backend. 

https://www.postgresql.org/download/

# Instalación

### Creando un entorno virtual

Utilizando la terminal, desde el directorio raíz del proyecto, correr el comando:

- python3 -m venv venv

Con esto se creará una carpeta llamada "venv" que contiene el entorno virtual de Python en el que
trabajará el proyecto.

### Entrando al entorno virtual

Desde el directorio raíz, ejecutar el comando:

- venv\Scripts\activate

Si todo ha salido bien, la terminal debería mostrar (venv) antes del path actual, de la forma:

- (venv) C:\Proyectos\MinorManage>

### Descargando dependencias

Una vez en el entorno virtual, ejecute los siguientes comandos para instalar las dependencias necesarias para el proyecto:

- pip install djangorestframework
- pip install django-cors-headers
- pip install psycopg2-binary
- pip install djangorestframework-simplejwt

### Configurando credenciales

En el directorio raíz del proyecto, cree un archivo con el nombre secrets.json. Este archivo guarda información sensible para la seguridad del proyecto, por lo que debe manejarse con cuidado.

Una vez creado el archivo, ingrese los campos: SECRET_KEY, DB_NAME, DB_USER y DB_PASSWORD.

SECRET_KEY:  Corresponde a un string que Django utiliza para ciertas operaciones.  
DB_NAME:     Corresponde al nombre de la base de datos en PostgreSQL a utilizar.  
DB_USER:     Corresponde al nombre de usuario autorizado por la base de datos a utilizar.  
DB_PASSWORD: Corresponde a la contraseña del usuario autorizado.

El archivo final deberá lucir de la siguiente manera:

>{  
>	"SECRET_KEY":  "Su clave secreta ",  
>	"DB_NAME":     "Su nombre de base de datos",  
>	"DB_USER":     "Su nombre de usuario",  
>	"DB_PASSWORD": "Su contraseña (DB)"  
>}

# Ejecución

Desde el directorio raíz del proyecto, y dentro del entorno virtual, ejecutar el comando:

- python3 manage.py runserver 8000