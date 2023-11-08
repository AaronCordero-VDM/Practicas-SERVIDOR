#!C:\Users\zx22student3208\AppData\Local\Programs\Python\Python311\python.exe

from BDvideojuegos import BDVideojuegos
import HtmlVideojuegos

import sys
import os
from urllib.parse import parse_qs

print("Content-type: text/html\n")

param = parse_qs(os.environ.get("QUERY_STRING"))

# acceder a la base de datos
bd = BDVideojuegos()
if ("nombre" in param and param["nombre"][0] != "" \
    and "empresa" in param and param["empresa"][0] != "" \
    and "tematica" in param and param["tematica"][0] != ""\
    and "id" in param and param["id"][0] != ""\
    and "numero_de_jugadores" in param and param["numero_de_jugadores"][0] != ""\
    and "publicacion" in param and param["publicacion"][0] != ""):
        nombre = param["nombre"][0]
        empresa = param["empresa"][0]
        tematica = param["tematica"][0]
        id = param["id"][0]
        numero_de_jugadores = param["numero_de_jugadores"][0]
        publicacion = param["publicacion"][0]
        bd.modificar(id,nombre,empresa,tematica,numero_de_jugadores,publicacion)
        HtmlVideojuegos.error("Datos modificados")

else:
    HtmlVideojuegos.error("Algun parametro no es correcto")


bd.cerrarBD()

