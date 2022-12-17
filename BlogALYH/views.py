from django.shortcuts import render
from django.http import HttpResponse
from BlogALYH.models import *

# Create your views here.

def inicio(request):
    return render(request, "BlogALYH/2index.html")

def acerca_de(request):
    return render(request, "BlogALYH/4acerca_de.html")

def registro_usuario(request):
    return render(request, "BlogALYH/3registro_usuario.html")