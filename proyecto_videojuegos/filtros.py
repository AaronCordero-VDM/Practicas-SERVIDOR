#!C:\Users\zx22student3208\AppData\Local\Programs\Python\Python311\python.exe

from BDvideojuegos import BDVideojuegos
import HtmlVideojuegos
import FormVideojuegos

print("Content-type: text/html\n")

bd = BDVideojuegos()

#   6. Mostrar 
HtmlVideojuegos.salidaPrincipal(bd.juegosConFiltro(FormVideojuegos.crearFiltros()))

# contenido de crear filtros en formVideojuegos.py (PASO 7)

 # cerrar conexion base de datos
bd.cerrarBD()