#!E:\Python3.11\python.exe

print("Content-Type: text/html\n")

import os, codigoHtml, json
from urllib.parse import parse_qs

param = parse_qs(os.environ.get("QUERY_STRING"))

cuenta = (param["1"][0])

try:
   fich = open("datos/listaCuentas.dat")
except:
   fich = open("datos/listaCuentas.dat","x")

if os.path.getsize("datos/listaCuentas.dat") != 0:
    cuentas = json.load(fich)
else:
    cuentas = []

                
codigoHtml.pagPrincipal()
print(cuenta)
print("<br>")
print(cuentas)
print("<br>")
if len(cuentas) > 0:
    listaCuentas = json.load(fich)
    listaJson = json.dumps(listaCuentas)
    print(listaJson)
    for a in (listaCuentas):
        cuentaActual = a
        print(cuentaActual)
        for b in cuentaActual:
            print(b)
codigoHtml.finHtml()