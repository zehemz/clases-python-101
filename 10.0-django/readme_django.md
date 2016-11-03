

https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface

http://stackoverflow.com/questions/6587507/how-to-install-pip-with-python-3


The Web Server Gateway Interface (WSGI) is a specification for simple and universal interface between web servers and web applications or frameworks for the Python programming language. It was originally specified in PEP 333[1] authored by Phillip J. Eby, and published on 7 December 2003. It has since been adopted as a standard for Python web application development. The latest version of the specification is v1.0.1, also known as PEP 3333, published on 26 September 2010.[2]


Django includes a lightweight web server you can use for testing, so you won’t need to set up Apache until you’re ready to deploy Django in production.

If you want to use Django on a production site, use Apache with mod_wsgi. mod_wsgi can operate in one of two modes: an embedded mode and a daemon mode. In embedded mode, mod_wsgi is similar to mod_perl – it embeds Python within Apache and loads Python code into memory when the server starts. Code stays in memory throughout the life of an Apache process, which leads to significant performance gains over other server arrangements. In daemon mode, mod_wsgi spawns an independent daemon process that handles requests. The daemon process can run as a different user than the Web server, possibly leading to improved security, and the daemon process can be restarted without restarting the entire Apache Web server, possibly making refreshing your codebase more seamless. Consult the mod_wsgi documentation to determine which mode is right for your setup. Make sure you have Apache installed, with the mod_wsgi module activated. Django will work with any version of Apache that supports mod_wsgi.


Saber que version de django esta instalada:
```
[12:55:14@]$ python3.5 -m django --version
```

Remover viejas versiones de django:

Conocer path:
```
[12:55:14@]$python3.5 -c "import django; print(django.__path__)"
```

Si no está instalado nos bajamos los modulos de django via pip:
```
[12:55:14@]$ sudo python3.5 -m pip install django
```

Verificamos la instalación y versión de django `[12:55:14@]$python3.5`:
```
>>> import django
>>> print(django.get_version())
1.10.1
```

Crear proyecto django (crea estructuras)
```
django-admin startproject lucasweb
```

Si tienen problemas con ejecutar django-admin:
1. Buscan el path de python para la version de python que esten ejecutando.
2. dentro de ese path tiene que existir la carpeta "bin"

Luego, desde allí, por ejemplo:
```
python3.5 /Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/django/bin/django-admin.py startproject lucasweb
```

Se genera la siguiente estructura de proyecto:
```
lucasweb/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        wsgi.py
```

Ejecutando la web:

```
[12:55:14@]$ python3.5 manage.py runserver
Performing system checks...
System check identified no issues (0 silenced).
You have 13 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
September 25, 2016 - 15:56:52
Django version 1.10.1, using settings 'lucasweb.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

Luego, podemos chequear que nuestra web está funcionando en: http://localhost:8000/ que es lo mismo que http://127.0.0.1:8000/

Otras configuraciones de ip-puerto en el servidor local:
python3.5 manage.py runserver 0.0.0.0:8000

[Django tutorial](https://docs.djangoproject.com/en/1.10/intro/tutorial01/)
[Django, verificando errores](https://docs.djangoproject.com/en/1.10/faq/troubleshooting/#troubleshooting-django-admin)


¿Cuál es la diferencia entre un proyecto y una aplicación? Una app es una aplicación web que hace algo, por ejemplo, un sistema de blog, una base de datos de registros públicos o una aplicación de encuesta simple. Un proyecto es un conjunto de configuraciones y aplicaciones para un sitio web determinado. Un proyecto puede contener aplicaciones múltiples. Una aplicación puede estar en varios proyectos.


Crear App:

```
[12:55:14@]$ python3.5 manage.py startapp miapp
```

Estructura:

```
miapp/
  __init__.py
  apps.py
  models.py
  views.py
  admin.py
  tests.py
  migrations/
    __init__.py  
```


1. Se agrega en miapp/views.py una función que retorne un HTTP response.
from django.http import HttpResponse

```
def index(request):
    return HttpResponse("yolo!!!")
```

2. Se agrega en `miapp/urls.py`

```
from django.conf.urls import url
from django.contrib import admin
from . import views #Estoy importando a que funcion llamar.
urlpatterns = [
    url(r'^$', views.index, name='index'), #Patron de macheo para llamar a mi funcion llamada index.
]

```

Buenisimo! ya tenes tu primera app, podes correrla desde Clases-Python-101/10.0-django/djangoWeb/lucasweb$ python3.5 manage.py runserver 0.0.0.0:8000

Take a look at virtualenv and virtualenvwrapper. These tools provide isolated Python environments, which are more practical than installing packages systemwide. They also allow installing packages without administrator privileges. The contributing tutorial walks through how to create a virtualenv on Python 3.

-----------------------------------------------------------
fin parte 1


Es probable que te de este mensaje sobre las migraciones.

```
Clases-Python-101/10.0-django/djangoWeb/lucasweb$ python3.5 manage.py runserver 0.0.0.0:8000
Performing system checks...

System check identified no issues (0 silenced).

You have 13 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
```

https://docs.djangoproject.com/es/1.10/intro/tutorial02/

Ver:
/Clases-Python-101/10.0-django/djangoWeb/lucasweb/lucasweb/settings.py

```
# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```
Como se puede ver, la configuración de la base de datos está generada para poder utilizar sqlite3.
Sin embargo, estos cambios no se harán efectivos hasta que no "migremos" a nuestra base de datos.

```
Clases-Python-101/10.0-django/djangoWeb/lucasweb$ python3.5 manage.py migrate
```

Creamos el superUser.
```
Clases-Python-101/10.0-django/djangoWeb/lucasweb$ python3.5 manage.py createsuperuser
Username: admin
Email address: admin@admin.com
Password:
Password (again):
Superuser created successfully.
```

10.0-django/djangoWeb/lucasweb/miapp/models.py


```
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

```

```
INSTALLED_APPS = [
    'miapp.apps.MiappConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

```

python3.5 manage.py makemigrations miapp


Al ejecutar makemigrations, usted le indica a Django que ha realizado algunos cambios a sus modelos (en este caso, ha realizado cambios nuevos) y que le gustaría que los guarde como una migración.

Django guarda los cambios en sus modelos como migraciones (y por lo tanto en su esquema de base de datos); son solo archivos en el disco. Usted puede leer la migración para su nuevo modelo si lo desea, es el archivo polls/migrations/0001_initial.py. No se preocupe, no se espera que usted las lea cada vez que Django hace una, sino que están diseñadas para que sean editables en caso de que usted desee modificar manualmente como Django cambia las cosas.

Hay un comando que ejecutará las migraciones para usted y gestionará el esquema de base de datos automáticamente; este se denomina migrate, y hablaremos de ello en un momento, pero primero, vamos a ver cuál SQL esa migración ejecutaría . El comando sqlmigrate recibe nombres de migración y devuelve su SQL:

python3.5 manage.py sqlmigrate miapp 0001

```
Clases-Python-101/10.0-django/djangoWeb/lucasweb$ python3.5 manage.py sqlmigrate miapp 0001
BEGIN;
--
-- Create model Choice
--
CREATE TABLE "miapp_choice" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "choice_text" varchar(200) NOT NULL, "votes" integer NOT NULL);
--
-- Create model Question
--
CREATE TABLE "miapp_question" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "question_text" varchar(200) NOT NULL, "pub_date" datetime NOT NULL);
--
-- Add field question to choice
--
ALTER TABLE "miapp_choice" RENAME TO "miapp_choice__old";
CREATE TABLE "miapp_choice" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "choice_text" varchar(200) NOT NULL, "votes" integer NOT NULL, "question_id" integer NOT NULL REFERENCES "miapp_question" ("id"));
INSERT INTO "miapp_choice" ("votes", "choice_text", "id", "question_id") SELECT "votes", "choice_text", "id", NULL FROM "miapp_choice__old";
DROP TABLE "miapp_choice__old";
CREATE INDEX "miapp_choice_7aa0f6ee" ON "miapp_choice" ("question_id");
COMMIT;
```

La salida exacta variará dependiendo de la base de datos que esté utilizando. El ejemplo anterior se genera para sqlite.

Los nombres de las tablas se generan automáticamente combinando el nombre de la aplicación (miapp) y el nombre del modelo en minúscula; question y choice. (Usted puede anular este comportamiento).

Las claves primarias (IDs) se agregan automáticamente. (Usted también puede anular esto).

Convencionalmente, Django añade "id" al nombre del campo de la clave externa ( sí, usted también puede anular esto).

La relación de la clave externa se hace explícita por una restricción``FOREIGN KEY``. No se preocupe por las partes “DEFERRABLE”; eso solo le indica a PostgreSQL que no aplique la clave externa hasta el final de la transacción.

Se adapta a la base de datos que está utilizando, así que los tipos de campos específicos de la bases de datos como auto_increment (MySQL), “serial” (PostgreSQL) o integer primary key autoincrement (SQLite) se gestionan de forma automática. Lo mismo se aplica para la cita de nombres de campos, por ejemplo, el uso de comillas dobles o comillas simples.

El comando :djadmin: sqlmigrate en realidad no ejecuta la migración en su base de datos, sólo la imprime en la pantalla para que pueda ver lo que SQL Django piensa que se requiere. Es útil para comprobar lo que Django va a hacer o si usted tiene administradores de bases de datos que requieran scripts SQL para introducir cambios.

Si le interesa, usted también puede ejecutar python manage.py check; este revisa cualquier problema en su proyecto sin hacer migraciones o modificar la base de datos.

A continuación, ejecute de nuevo migrate para crear esas tablas modelos en su base de datos:

python3.5 manage.py migrate

10.0-django/djangoWeb/lucasweb/miapp/admin.py
```
from .models import Question

admin.site.register(Question)
```


PermissionError at /admin/miapp/contact/add/

[Errno 13] Permission denied: '/media/photos'

Request Method: 	POST
Request URL: 	http://localhost:8000/admin/miapp/contact/add/
Django Version: 	1.10.2
Exception Type: 	PermissionError
Exception Value: 	

[Errno 13] Permission denied: '/media/photos'

Exception Location: 	/usr/lib/python3.5/os.py in makedirs, line 241
Python Executable: 	/usr/bin/python3.5
Python Version: 	3.5.2
Python Path: 	

['/home/lucas/Documents/Clases-Python-101/10.0-django/djangoWeb/lucasweb',
 '/usr/lib/python35.zip',
 '/usr/lib/python3.5',
 '/usr/lib/python3.5/plat-x86_64-linux-gnu',
 '/usr/lib/python3.5/lib-dynload',
 '/home/lucas/.local/lib/python3.5/site-packages',
 '/usr/local/lib/python3.5/dist-packages',
 '/usr/lib/python3/dist-packages']


Agregar str function a un modelo.
Agregar modelos a admin.py
Ahora, crear templates


manage.py shell
