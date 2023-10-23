#!C:\Users\zx22student3208\AppData\Local\Programs\Python\Python311\python.exe

print("Content-Type: text/html\n")

import os,codigoHtml , json

#Abrimos el archivo de datos
try:
   fich = open("datos/listaCuentas.dat")
except:
   fich = open("datos/listaCuentas.dat","x")

#Si el archivo tiene algo escrito
if os.path.getsize("datos/listaCuentas.dat") != 0:
    #Guardamos el contenido en un array desde un formato JSON
    cuentas = json.load(fich)
else:
    #Si no, creamos el array en blanco
    cuentas = []
#Cerramos el fichero
fich.close()

#Funcion para crear las opciones del select segun las cuentas que hayan creadas en el JSON
def listaDeCuentas():
        #Hacemos un bucle para recorrer las cuentas
        for p in cuentas:
            #Creamos el option para la cuenta con el numero de la misma
            print("<option value='")
            print(f"{p[1]}'>{p[1]}")
            print("</option>")

#Funcion para listar las cuentas disponibles
def listarCuentas():
    #Si hay cuentas disponibles
    if len(cuentas) != 0:
        #Creamos una tabla para guardar las cuentas 
        print("<table><th>ID</th><th>Numero de cuenta</th><th>Saldo</th><th>Informacion</th>")
        #Recorrermos las cuentas
        for p in cuentas:
            #Creamos cada fila con sus datos para la cuenta
            print(f"<tr><td id='contCuenta' name='contCuenta'>{p[0]}</td>")
            print(f"<td class='numcuenta'>{p[1]}</td>")
            print(f"<td class='cantidad'>{p[2]} Euros</td>")
            print("<td><form action='infoCuenta.py'>")
            print(f"<button class='info' for='{p[0]}'>Ver cuenta</button>")
            print(f"<input value='{p[1]}' name='id' id='{p[0]}' style='display: none'>")
            print("</form></td></tr>")
    #Si no hay cuentas disponibles
    else:
        print("<h3>No hay cuentas disponibles</h3><br>")

#Llamamos a las funciones para escribir en html
codigoHtml.pagPrincipal()
codigoHtml.listarCuentasInicio()
listarCuentas()
codigoHtml.listarCuentasFin()

codigoHtml.operacionesInicio()
listaDeCuentas()
codigoHtml.operacionesFin()
codigoHtml.finHtml()
