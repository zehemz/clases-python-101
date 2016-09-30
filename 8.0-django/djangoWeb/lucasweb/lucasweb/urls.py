"""lucasweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include #Agregado...
from django.contrib import admin


urlpatterns = [
    #Agregado
    url(r'^miapp/', include('miapp.urls')),
    url(r'^admin/', admin.site.urls), #Salvo este, vaya dios a saber por que django se pasa
]


##demo linter
def agarrame_la_milanga(agarrame_la_milanga_express):
    '''agarrame_la_milanga'''
    agarrame_la_milanga_express = 3
    print(agarrame_la_milanga_express)
