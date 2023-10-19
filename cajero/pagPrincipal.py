#!E:\Python3.11\python.exe

print("Content-Type: text/html\n")

import os,codigoHtml , json


try:
   fich = open("datos/listaCuentas.dat")
except:
   fich = open("datos/listaCuentas.dat","x")

if os.path.getsize("datos/listaCuentas.dat") != 0:
    cuentas = json.load(fich)
else:
    cuentas = []

fich.close()


def listaDeCuentas():
    if len(cuentas) != 0:
        for p in cuentas:
            print("<option value='")
            print(f"{p[0]}'>{p[0]}")
            print("</option>")
    else:
        print("<h3>No hay cuentas disponibles</h3>")
    print("<hr>")

def listarCuentas():
    contador = 1
    if len(cuentas) != 0:
        for p in cuentas:
            print(f"<textfield id='contCuenta' name='contCuenta'>{contador}</textfield>")
            print(f"<label for='numcuenta'>Numero de cuenta:</label> <textfield class='numcuenta'>{p[0]}</textfield>")
            print(f"<label for='cantidad'>Saldo:</label><textfield class='cantidad'>{p[1]} Euros</textfield>")
            print("<form action='infoCuenta.py'>")
            print(f"<button for='{contador}'>Ver cuenta</button>")
            print(f"<input value='{p[0]}' name='{contador}' id='{contador}' style='display: none'>")
            print("</form>")
            contador += 1
        return p
    else:
        print("<h3>No hay cuentas disponibles</h3>")

codigoHtml.pagPrincipal()
codigoHtml.listarCuentasInicio()
listarCuentas()
codigoHtml.listarCuentasFin()

codigoHtml.operacionesInicio()
listaDeCuentas()
codigoHtml.operacionesFin()
codigoHtml.finHtml()
