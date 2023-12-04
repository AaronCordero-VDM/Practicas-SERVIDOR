#!C:\Users\zx22student3208\AppData\Local\Programs\Python\Python311\python.exe

from urllib.parse import parse_qs
import os
import http.cookies

param = parse_qs(os.environ.get('QUERY_STRING'))
palabra = param["palabra"][0]
cookie = http.cookies.SimpleCookie()

def crearVocales():
    cookie["palabrasVocales"] = str(palabra)

def crearConsonantes():
    cookie["palabrasConsonantes"] = str(palabra)

if (palabra.lower()).startswith("a") or (palabra.lower()).startswith("e") or (palabra.lower()).startswith("i") or (palabra.lower()).startswith("o") or (palabra.lower()).startswith("u"):
    if os.environ.get("HTTP_COOKIE") != None: # Si existen cookies ya creadas, las carga
        cookie.load(os.environ.get("HTTP_COOKIE"))
        if "palabrasVocales" in cookie: # Si la cookie palabrasVocales está creada, le añade el nuevo valor
            cookie["palabrasVocales"] = str(cookie["palabrasVocales"].value)+" " + palabra
        else: # Si la cookie palabrasVocales no está creada, la crea con el nuevo valor
            crearVocales()
    else: # Si no existen cookies ya creadas, crea la cookie palabrasVocales con el nuevo valor
        crearVocales()
    print("Content-type: text/html") # Imprime la cabecera html necesaria para la cookie
    print(cookie) # Imprime la cookie
    print() # Imprime una linea en blanco

else:
    if os.environ.get("HTTP_COOKIE") != None: # Si existen cookies ya creadas, las carga
        cookie.load(os.environ.get("HTTP_COOKIE"))
        if "palabrasConsonantes" in cookie: # Si la cookie palabrasConsonantes está creada, le añade el nuevo valor
            cookie["palabrasConsonantes"] = str(cookie["palabrasConsonantes"].value)+" "+ palabra
        else: # Si la cookie palabrasConsonantes no está creada, la crea con el nuevo valor
            crearConsonantes()
    else: # Si no existen cookies ya creadas, crea la cookie palabrasConsonantes con el nuevo valor
        crearConsonantes()
    print("Content-type: text/html") # Imprime la cabecera html necesaria para la cookie
    print(cookie) # Imprime la cookie
    print() # Imprime una linea en blanco

print("""
<html>
    <head>
        <meta http-equiv="refresh" content="0;formulario_palabras.html"/>
    </head>
</html>
""")