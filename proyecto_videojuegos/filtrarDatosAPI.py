#!C:\Users\zx22student3208\AppData\Local\Programs\Python\Python311\python.exe

from BDvideojuegos import BDVideojuegos
import json
import FormVideojuegos


bd = BDVideojuegos()

miresultado = bd.juegosConFiltro(FormVideojuegos.crearFiltros())

print(json.dumps(miresultado))

bd.cerrarBD()