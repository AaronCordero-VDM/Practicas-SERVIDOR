#!E:\Python3.11\python.exe

import os, json, codigoHtml, random

    
def crearCuenta():
    numero = "ES"
    for n in range(20):
        n = (random.randint(0, 9))
        numero+=str(n)
    cuenta = [numero,0]

    if os.path.getsize("datos/listaCuentas.dat") == 0:
        listaCuentas = [cuenta]
        listaJson = json.dumps(listaCuentas)

    else:
        fich = open("datos/listaCuentas.dat")
        listaCuentas = json.load(fich)
        listaCuentas.append(cuenta)
        listaJson = json.dumps(listaCuentas)
    fich = open("datos/listaCuentas.dat","wt")
    fich.write(listaJson)
    fich.close()

crearCuenta()
codigoHtml.recarga()