#!C:\Users\zx22student3208\AppData\Local\Programs\Python\Python311\python.exe

# Este python crea una lista donde muestra los valores de las cookies "palabrasVocales" y "palabrasConsonantes"

import http.cookies
import os

print("Content-type: text/html\n")

cookie = http.cookies.SimpleCookie()

if os.environ.get("HTTP_COOKIE") is not None: # Si hay cookies creadas las carga y crea la lista
    cookie.load(os.environ.get("HTTP_COOKIE")) # Carga las cookies del sistema
    # Crea la lista de las vocales
    lista1 = "<h1>Valores de la cookie palabrasVocales</h1><ul>"
    for valor in cookie["palabrasVocales"].value.split(" "): # Primero separa los valores de la cookie por los espacios, luego recorre ese array con los valores para crear los li
        lista1 += f"<li>{valor}</li>"
    lista1 += "</ul>"

    # Crea la lista de las consonantes
    lista2 = "<h1>Valores de la cookie palabrasConsonantes</h1><ul>"
    for valor in cookie["palabrasConsonantes"].value.split(" "):
        lista2 += f"<li>{valor}</li>"
    lista2 += "</ul>"
    print(lista1)
    print(lista2)
else: # Si no hay cookies creadas muestra un mensaje de error
    print("<h1>No hay valores en las cookies</h1>")