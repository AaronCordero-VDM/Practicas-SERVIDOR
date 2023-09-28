#!C:\Users\zx22student3208\AppData\Local\Programs\Python\Python311\python.exe

print("Content-Type: text/html\n")

import os
from urllib.parse import parse_qs
from math import sqrt

param = parse_qs(os.environ.get("QUERY_STRING"))

dato = param["dato"][0]

equiposFutbolBuenos = "Sporting Madrid Barça Atletico Betis Sevilla"


#Tupla: una lista de objetos incambiables pero admiten duplicados, y esta siempre ordenada
#sin poder modificar el orden de la lista
x = {"apple", "banana", "cherry"}

#Lista de objetosesta siempre ordenada sin poder modificar el orden de la lista,
#puedes cambiar el contenido y permite duplicados
list = ["apple", "banana", "cherry"]

#Set no permite tener duplicados, tampoco puedes cambiar el contenido ni el orden
set = {"apple", "banana", "cherry"}

#Prints tipos

if dato not in equiposFutbolBuenos:
    print("EL equipo "+ dato + " no es bueno")
    print("EL equipo {} no es bueno".format(dato))
    print(f"El equipo {dato} no es bueno")
else:
    print(f"El eqipo {dato} es bueno")

print(equiposFutbolBuenos[10:15]+"<br/>")
print(equiposFutbolBuenos[10:]+"<br/>")
print(equiposFutbolBuenos[:15]+"<br/>")

print(equiposFutbolBuenos.strip()+"<br/>")

print(equiposFutbolBuenos.replace("i","000")+"<br/>")
print(equiposFutbolBuenos.split(" ")[2]+"<br/>")

print(dato.isdecimal())
print(dato.isdigit())

