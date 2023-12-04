#!C:\Users\zx22student3208\AppData\Local\Programs\Python\Python311\python.exe

#Ejercicio 1, mostrar mediante un bucle las 20 imagenes de una galeria de coches

print("Content-type: text/html\n")

import os
from urllib.parse import urlparse, unquote, parse_qs

#Imprimimos el comienzo del html
print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Ejercicio1</title>
</head>
<body>
      <h1>Ejercicio1</h1>
""")

#bucle apra recorrer las 20 imagenes con un range de 21 ya que el ulltimo no esta incluido
for coche in range(21):
    #Como el range empieza en 0 cuando sea mayo que cero cogeremos la imagen 
    if coche > 0:
        #Imprimimos el div con su id y la imagen con su alt y su ruta
        print(f"<div id='contenedor{coche}'><img src='imagen/coche{coche}' alt='imagen de coche {coche}'></img></div>")

#Imprimimos el final del html
print("""
</body>
</html>
""")