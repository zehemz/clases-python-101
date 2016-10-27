from django.shortcuts import render
# Create your views here.
'''Agregado.....'''
from django.http import HttpResponse

def index(request):
    return HttpResponse("yolo!!!")
