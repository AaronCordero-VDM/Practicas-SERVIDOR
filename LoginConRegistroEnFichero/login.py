#!C:\Users\zx22student3208\AppData\Local\Programs\Python\Python311\python.exe

#importaciones
import os, json
import hashlib
import http.cookies
import uuid

from urllib.parse import urlparse, parse_qs

import codigoHtml

ru = os.environ.get("REQUEST_URI")

parametros = urlparse(ru)
param = parse_qs(parametros[4])

#fichero con usuarios
fichUsu = "usuarios.json"

#comprobar que vienen todos los parametros
if "nombre" not in param:
    #le pasamos el mensaje al html donde pone texto
    codigoHtml.error("Falta el nombre")
    exit() # sale del python(de la ejecucion)
if "password" not in param:
    #le pasamos el mensaje al html donde pone texto
    codigoHtml.error("Falta la contraseña")
    exit() # sale del python(de la ejecucion)

#parametros de la url a leer
nombre = param["nombre"][0]
contraseña = param["password"][0]
#encriptarmos la contraseña
contraseñaEncriptada = (hashlib.sha512(str.encode(contraseña)).hexdigest())

#funcion que que obtiene los usuarios registrados del fichero
with open(fichUsu) as fichero:
    try:
        #convierto el fichero json a una lista
        listaUsuarios = json.load(fichero)
    except:
        #crea la lista vacia
        listaUsuarios = []

#variable booleana
usuarioEncontrado = False

for usu in listaUsuarios:
    #si el aparametro guardado en la variable coincide con el nombre de la lista
    #si encuentra la coincidencia se para, no sigue
    if(usu[0] == nombre and usu[1] == contraseñaEncriptada):
        usuarioEncontrado = True
        #sin el esto me imprime el usuario que no busco
        break

#si ya encuentra el usuario
if not usuarioEncontrado:
    #te imprime
    print("Usuario no encontrado")

#crea la cookie para el control de sesion
print("Content-Type: text/html")
cookie = http.cookies.SimpleCookie()
cookie["Usuario"] = uuid.uuid4()
print(cookie)
print()
print("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">          
        <meta http-equiv="refresh" content="2;pagina1.py">
        <link rel="stylesheet" href="css/style.css">
        <title>Login con registro</title>
        </head>
    <body>
    </body>
    </html>
""")
codigoHtml.correcto()