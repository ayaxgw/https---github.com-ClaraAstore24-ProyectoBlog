from django.shortcuts import render
from django.http import HttpResponse
from BlogALYH.models import *

# Create your views here.

def inicio(request):
    return render(request, "BlogALYH/2index.html")

def acerca_de(request):
    return render(request, "BlogALYH/4acerca_de.html")

def registro_usuario(request):
    if request.method == "POST":
        nombre_usuario = request.POST["Nombre"]
        usuario_email = request.POST["Email"]
        usuario_contraseña = request.POST["Contraseña"]

        usuario = Registrar(nombre = nombre_usuario, email = usuario_email, contraseña = usuario_contraseña)
        usuario.save()

    return render(request, "BlogALYH/3registro_usuario.html")

def buscar_publicacion(request):
    return render(request, "BlogALYH/5busqueda_publicacion.html")

def resultado_buscar_publicacion(request):
    nombre_publicacion = request.GET["nombre_publicacion"]

    publicaciones = Publicaciones.objects.filter(comentarios__icontains=nombre_publicacion)

    return render(request,"BlogALYH/6resultados_buscar_publicacion.html",
    {"publicaciones":publicaciones})