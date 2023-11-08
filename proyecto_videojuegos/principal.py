#!C:\Users\zx22student3208\AppData\Local\Programs\Python\Python311\python.exe

from BDvideojuegos import BDVideojuegos
import HtmlVideojuegos

print("Content-type: text/html\n")

bd = BDVideojuegos()

#   2. Pido todos los datos para comprobar que los recibo !!
##print(str(bd.todosLosVideojuegos())) # lista de tuplas !!

#   Paso 3 -> en HtmlVideojuegos.py

#   4.  LLamamos a salida principal del htmlVideojuegos y 
#       le pasamos el contenido que nos traia en el paso 2 (la lista de tuplas)
HtmlVideojuegos.salidaPrincipal(bd.todosLosVideojuegos())



#   Paso 5 -> en BDvideojuegos.py

 # cerrar conexion base de datos
bd.cerrarBD()