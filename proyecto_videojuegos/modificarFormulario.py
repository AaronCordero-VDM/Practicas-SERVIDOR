#!C:\Users\zx22student3208\AppData\Local\Programs\Python\Python311\python.exe

from BDvideojuegos import BDVideojuegos
import HtmlVideojuegos

import sys
import os
from urllib.parse import parse_qs
import HtmlVideojuegos
# acceder a la base de datos
bd = BDVideojuegos()

print("Content-type: text/html\n")

param = parse_qs(os.environ.get("QUERY_STRING"))

if "id" in param and param["id"][0] != "":
    # capturar el id a borrar
    id = param["id"][0]
    HtmlVideojuegos.formularioModificar(bd.seleccionarPorId(id))
else:
    HtmlVideojuegos.error("Falta el id para modificar")
# cerrar conexion base de datos
bd.cerrarBD()