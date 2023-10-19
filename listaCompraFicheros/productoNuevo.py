#!C:\Users\zx22student3208\AppData\Local\Programs\Python\Python311\python.exe

print("Content-Type: text/html\n")

import codigoHtml

import os
from urllib.parse import urlparse, unquote, parse_qs

ru = os.environ.get("REQUEST_URI")
parametros = urlparse(ru)
param = parse_qs(parametros[4])

prod = param["producto"][0]
cant = param["cantidad"][0]

try:
    fich = open("datos/listaCompra.dat","at")
except:
    print("Error")

if os.path.getsize("datos/listaCompra.dat") != 0:
    fich.write("\n")

fich.write(prod+";"+cant)

fich.close

codigoHtml.recarga()


