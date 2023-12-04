#!C:\Users\zx22student3208\AppData\Local\Programs\Python\Python311\python.exe

from urllib.parse import parse_qs
import os

print("Content-type: text/html\n")

param = parse_qs(os.environ.get('QUERY_STRING'))

# Comprobamos la validez de los datos del input
if "tipo" not in param or param["tipo"][0] == "":
    print("""
    <html>
        <head>
            <meta http-equiv="refresh" content="2;form5.html"/>
        </head>
        <body>
            <h1>Rellena los campos</h1>
        </body>
    </html>
    """)
    exit()

tipo = (param["tipo"][0])

# Inicializamos el total de los precios
total = 0
# Abrimos el fichero en modo lectura
with open("numeros.dat","r") as file: 
    # quitamos los saltos de linea que hay en el fichero a la vez que leemos las distintas lineas
    numeros = [num.strip('\n') for num in file.readlines()]
    # recorremos la lista de los numeros
    for num in numeros:
        # dividimos el numero en sus dos partes, el numero y la letra por el espacio " "
        numero = num.split(" ")
        # Si la letra del numero que es la posicion 1 despues del split, coincide con el tipo seleccionado, se suma al total
        # la parte numerica del split es decir la posicion 0
        if (str(numero[1])).upper() == tipo:
            total += int(numero[0])
    print(f"Suma realizada: {total}")
    # abrimos el fichero del resultado y escribimos el total
    with open("resultado.dat","wt") as file:
        file.write(f"Total: {total}\n")

