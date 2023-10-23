#!C:\Users\zx22student3208\AppData\Local\Programs\Python\Python311\python.exe

print("Content-type: text/html\n")

import os, codigoHtml, json
import requests
from urllib.parse import parse_qs

param = parse_qs(os.environ.get("QUERY_STRING"))

#Guardamos los parametros aue le pasa el form para operar
cuenta = (param["cuenta"][0])
cantidad = (param["cantidad"][0])
concepto = (param["concepto"][0])
operacion = str(param["operacion"][0])

#Abrimos el archivo de datos
try:
   fich = open("datos/listaCuentas.dat")
except:
   fich = open("datos/listaCuentas.dat","x")

#Compramos si el archivo esta vacio
if os.path.getsize("datos/listaCuentas.dat") != 0:
    #Guardamos el contenido en un array desde un formato JSON
    listaCuentas = json.load(fich) #Cargamos el fichero JSON en un array
else:
    #Si no, creamos el array en blanco
    listaCuentas = []
    listaJson = []


#Si la cantidad no contiene caracteres
if (cantidad.find("e")<0):
    #Primera comparacion, si la cantidad es mayor que 0
    if int(cantidad) > 0:
        #Si hay una cuenta seleccionada
        if cuenta.lower() != "ninguna":
            for a in (listaCuentas):#Recorremos las lista de las cuentas
                for b in a:#Recorremos los valores de cada cuenta
                    if b == cuenta.strip():#Si la cuenta del bucle es igual a la cuenta seleccionada
                        pos = listaCuentas.index(a)
                        #Si la oprecion es ingrasar
                        if operacion == "ingresar":
                            nuevaCant = int(cantidad) + int(a[2]) #La nueva cantidad sera la cantidad introducida "cantidad" mas el saldo de la cuenta "a"
                            listaCuentas[b[0]].append("+ "+concepto+" : "+cantidad)#Guardamos la operacion como una nueva posicion en la cuenta
                        #Si la oprecion es retirar
                        elif operacion == "retirar":
                            nuevaCant = int(a[2]) - int(cantidad)#La nueva cantidad sera la cantidad introducida "cantidad" menos el saldo de la cuenta "a"
                            #Si la nueva cantidad es negativa, entonces no podras retirar el dinero
                            if nuevaCant < 0:
                                print("<h2>No hay saldo suficiente</h2>")
                                codigoHtml.recargaSinCambios()
                                break
                            listaCuentas[b[0]].append("- "+concepto+" : "+cantidad)#Guardamos la operacion como una nueva posicion en la cuenta
                        listaCuentas[b[0]][2]=nuevaCant#Guardamos e nuevo saldo en la posicion que corresponde al saldo de la cuenta
                        listaJson = json.dumps(listaCuentas)#Transformamos el archivo en formato JSON
                        fich = open("datos/listaCuentas.dat","wt")#Sobrescribimos la lista en el archivo
                        fich.write(listaJson)
                        codigoHtml.recarga()
                        fich.close()#Cerramos el fichero

        #Si no hay cuentas creadas
        else:
            print("<h2>No hay cuentas para operar</h2>")
            codigoHtml.recargaSinCambios()
    #Si la cantidad es menor o igual que 0
    else:
        print("<h1>No se aceptan cantidades negativas o nulas</h1>")
        codigoHtml.recargaSinCambios()
#Si la cantidad tiene letras
else:
    print("<h1>No se admiten cantidades como caracteres</h1>")
    codigoHtml.recargaSinCambios()