from django.urls import path 
from BlogALYH.views import *

urlpatterns = [
    path("Inicio/", inicio, name="iniciar"),
    path("Usuario/", registro_usuario, name="usuario"),
    path("Nosotros/", acerca_de, name="nosotros"),
    path("Buscar/", buscar_publicacion, name = "buscar"),
    path("Resultados/", resultado_buscar_publicacion, name = "resultado"),

]