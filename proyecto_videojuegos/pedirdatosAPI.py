#!C:\Users\zx22student3208\AppData\Local\Programs\Python\Python311\python.exe

from BDvideojuegos import BDVideojuegos
import json
print ("Content-Type: text/html\n")

bd = BDVideojuegos()

miresultado = bd.todosLosVideojuegos()

print(json.dumps(miresultado))

bd.cerrarBD()