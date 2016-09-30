'''
Generado por Lucas
'''
from django.conf.urls import url
from . import views #Estoy importando a que funcion llamar.

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
