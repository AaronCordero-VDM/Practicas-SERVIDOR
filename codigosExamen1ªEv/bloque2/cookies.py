#!C:\Users\zx22student3208\AppData\Local\Programs\Python\Python311\python.exe
import os
import hashlib
import http.cookies
import uuid

from urllib.parse import urlparse, parse_qs

ru = os.environ.get("REQUEST_URI")

parametros = urlparse(ru)
param = parse_qs(parametros[4])


#crea la cookie para el control de sesion
print("Content-Type: text/html")
cookie = http.cookies.SimpleCookie()
cookie["Usuario"] = uuid.uuid4()
print(cookie)
nombre = param["nombre"][0]
contraseña = param["password"][0]
#encriptarmos la contraseña
contraseñaEncriptada = (hashlib.sha512(str.encode(contraseña)).hexdigest())


#Eliminar la cookie
cookie = http.cookies.SimpleCookie()
cookie["Usuario"] = 1
cookie["Usuario"]["expires"] =  "Wed, 11 Oct 2022 07:28:00 GMT"