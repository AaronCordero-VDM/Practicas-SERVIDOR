#!E:\Python3.11\python.exe
print("Content-type: text/html\n")


import os, codigoHtml, json
import requests
from urllib.parse import parse_qs

param = parse_qs(os.environ.get("QUERY_STRING"))

cuenta = (param["cuenta"][0])
cantidad = (param["cantidad"][0])


def comprobarOper():
    if requests.get == 'POST':
        if 'confirmar' in requests.form:
            operacion=requests.form['operacion']
            return operacion
            
try:
   fich = open("datos/listaCuentas.dat")
except:
   fich = open("datos/listaCuentas.dat","x")

comprobarOper()
operacion = (param["operacion"][0])


if int(cantidad) > 0 and operacion != "":
    listaCuentas = json.load(fich)
    listaJson = json.dumps(listaCuentas)
    for a in (listaCuentas):
        cuentaActual = a
        for b in cuentaActual:
            if b == cuenta.strip():
                pos = listaCuentas.index(a)
                if operacion == "ingresar":
                    nuevaCant = int(cantidad) + int(cuentaActual[1])
                    listaCuentas[pos].append("+ Ingreso: "+cantidad)
                elif operacion == "retirar":
                    nuevaCant = int(cuentaActual[1]) - int(cantidad)
                    listaCuentas[pos].append("- Retirada: "+cantidad)
                listaCuentas[pos][1]=nuevaCant
                listaJson = json.dumps(listaCuentas)
                fich = open("datos/listaCuentas.dat","wt")
                fich.write(listaJson)
                codigoHtml.recarga()
                fich.close()
else:
    print("<h1>No se aceptan cantidades negativas</h1>")
    print("<h2>porqueeeee</h2>")
    codigoHtml.recarga()


        
