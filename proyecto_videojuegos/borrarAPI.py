#!C:\Users\zx22student3208\AppData\Local\Programs\Python\Python311\python.exe

from BDvideojuegos import BDVideojuegos
import HtmlVideojuegos

import json
import sys
import os
from urllib.parse import parse_qs

print("Content-type: text/html\n")

param = parse_qs(os.environ.get("QUERY_STRING"))

# acceder a la base de datos
bd = BDVideojuegos()

if "id" in param and param["id"][0] != "":
    # capturar el id a borrar
    id = param["id"][0]
    # borro el id
    bd.borrarPorId(id)

    print(json.dumps(True))
else:
    print(json.dumps(False))
    

# cerrar conexion base de datos
bd.cerrarBD()
