
Django includes a lightweight web server you can use for testing, so you won’t need to set up Apache until you’re ready to deploy Django in production.

If you want to use Django on a production site, use Apache with mod_wsgi. mod_wsgi can operate in one of two modes: an embedded mode and a daemon mode. In embedded mode, mod_wsgi is similar to mod_perl – it embeds Python within Apache and loads Python code into memory when the server starts. Code stays in memory throughout the life of an Apache process, which leads to significant performance gains over other server arrangements. In daemon mode, mod_wsgi spawns an independent daemon process that handles requests. The daemon process can run as a different user than the Web server, possibly leading to improved security, and the daemon process can be restarted without restarting the entire Apache Web server, possibly making refreshing your codebase more seamless. Consult the mod_wsgi documentation to determine which mode is right for your setup. Make sure you have Apache installed, with the mod_wsgi module activated. Django will work with any version of Apache that supports mod_wsgi.

Saber que version de django esta instalada: python3.5 -m django --version

Remover viejas versiones de django:

Conocer path: python3.5 -c "import django; print(django.__path__)"

Si no está instalado nos bajamos los modulos de django via pip:

sudo python3.5 -m pip install django

...python3.5
>>> import django
>>> print(django.get_version())
1.10.1

Crear proyecto django (crea estructuras)
django-admin startproject lucasweb

Si tienen problemas con ejecutar django-admin:
1) Buscan el path de python para la version de python que esten ejecutando.
2) dentro de ese path tiene que existir la carpeta "bin"
Luego, desde allí, por ejemplo:

python3.5 /Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/django/bin/django-admin.py startproject lucasweb


Se genera la siguiente estructura de proyecto:
lucasweb/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        wsgi.py

Ejecutando la web:
[12:55:14@lucasweb (master *)]$ python3.5 manage.py runserver
Performing system checks...

System check identified no issues (0 silenced).

You have 13 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.

September 25, 2016 - 15:56:52
Django version 1.10.1, using settings 'lucasweb.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

Luego, podemos chequear que nuestra web está funcionando en: http://localhost:8000/ que es lo mismo que http://127.0.0.1:8000/

Otras configuraciones de ip-puerto en el servidor local:
python3.5 manage.py runserver 0.0.0.0:8000

https://docs.djangoproject.com/en/1.10/intro/tutorial01/
https://docs.djangoproject.com/en/1.10/faq/troubleshooting/#troubleshooting-django-admin


¿Cuál es la diferencia entre un proyecto y una aplicación? Una app es una aplicación web que hace algo, por ejemplo, un sistema de blog, una base de datos de registros públicos o una aplicación de encuesta simple. Un proyecto es un conjunto de configuraciones y aplicaciones para un sitio web determinado. Un proyecto puede contener aplicaciones múltiples. Una aplicación puede estar en varios proyectos.

$python3.5 manage.py startapp miapp

miapp/
  __init__.py
  apps.py
  models.py
  views.py
  admin.py
  tests.py
  migrations/
    __init__.py  


-Se agrega en miapp/views.py una función que retorne un HTTP response.
from django.http import HttpResponse

def index(request):
    return HttpResponse("yolo!!!")

-Se agrega en miapp/urls.py

from django.conf.urls import url
from django.contrib import admin
from . import views #Estoy importando a que funcion llamar.
urlpatterns = [
    url(r'^$', views.index, name='index'), #Patron de macheo para llamar a mi funcion llamada index.
]


Take a look at virtualenv and virtualenvwrapper. These tools provide isolated Python environments, which are more practical than installing packages systemwide. They also allow installing packages without administrator privileges. The contributing tutorial walks through how to create a virtualenv on Python 3.
