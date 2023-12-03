#!C:\Users\zx22student3206\AppData\Local\Programs\Python\Python311\python.exe

# Este python crea una lista donde muestra los valores de la cookie "empiezaABC"

import http.cookies
import os

print("Content-type: text/html\n")

cookie = http.cookies.SimpleCookie()

if os.environ.get("HTTP_COOKIE") is not None: # Si hay cookies creadas las carga y crea la lista
    cookie.load(os.environ.get("HTTP_COOKIE")) # Carga las cookies del sistema

    # Crea la lista
    lista = "<h1>Valores de la cookie</h1><ul>"
    for valor in cookie["empiezaABC"].value.split(" "): # Primero separa los valores de la cookie por los espacios, luego recorre ese array con los valores para crear los li
        lista += f"<li>{valor}</li>"
    lista += "</ul>"

    print(lista)
else: # Si no hay cookies creadas muestra un mensaje de error
    print("<h1>No hay valores en la cookie</h1>")