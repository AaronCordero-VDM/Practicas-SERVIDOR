#!C:\Users\zx22student3208\AppData\Local\Programs\Python\Python311\python.exe


import os, json, codigoHtml, random

#Funcion para contar el id de las cuentas
def id():
    #Declaraos un contador que empiece en 1
    contador = 1
    #Si el archivo contiene algo
    if os.path.getsize("datos/listaCuentas.dat") != 0:
        #abrimos el archivo para leer
        fich = open("datos/listaCuentas.dat")
        #Cargamos el contenido en un array
        listaCuentas = json.load(fich)
        #Bucle para recorrer las cuentas
        for c in listaCuentas:
            contador += 1
    #Devuelve el valor contador
    return contador

#funcion para crear cuentas
def crearCuenta():
    #Introducimos el prfijo de la cuenta
    numero = "ES"
    #Bucle para crear los 20 digitos de la cuenta
    for n in range(20):
        n = (random.randint(0, 9))#Random entre 0 y 9 para dar un numero
        numero+=str(n)#Concatenamos los numeros con el prefijo
        #Creamos la cuenta con el id, el numero y el saldo
    cuenta = [id(),numero,0]
    return cuenta
#si el archivo esta vacio
if os.path.getsize("datos/listaCuentas.dat") == 0:
    #Creamos la lista de la cuenta vacia
    listaCuentas = [crearCuenta()]
    listaJson = json.dumps(listaCuentas)
#Si no esta vacio
else:
    fich = open("datos/listaCuentas.dat")#Abrimos y leemos el archivo
    listaCuentas = json.load(fich)#Cargamos el JSON en un array
    listaCuentas.append(crearCuenta())#Metemos la nueva cuenta en el array de las cuentas
    listaJson = json.dumps(listaCuentas)#Lo convertimos en un array util para JSON
fich = open("datos/listaCuentas.dat","wt")#Lo escribimos en el fichero
fich.write(listaJson)
fich.close()

crearCuenta()
codigoHtml.recarga()