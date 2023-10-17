#!C:\Users\zx22student3208\AppData\Local\Programs\Python\Python311\python.exe

print("Content-Type: text/plain\n")

import os
from urllib.parse import parse_qs
from math import sqrt

param = parse_qs(os.environ.get("QUERY_STRING"))

fig = int(param["figura"][0])
nFil = int(param["nFilas"][0])

#dibuja un cuadrado de asteriscos de n filas y n columnas
def cuadrado(n):

    linea = "" #variable que contiene una fila

    print(f"Dibujar un cuadrado de {nFil} filas y {nFil} columnas")
    for f in range(n): #bucle para crear las filas
        #for c in range(n): bucle para crear las columnas
        #    linea += "*"
        #print(linea)
        linea += "*" * n
        print(linea)
        linea = "" #vaciar la linea una vez impresa

def triangulo(n):
    print(f"Dibujar un triangulo de {nFil} filas")
    linea = ""

    for f in range(n):
        #for c in range(f+1):
        #    linea += "*"
        #print(linea)
        linea += "*" * (f+1)
        print(linea)
        linea = "" #vaciar la linea una vez impresa   

def trianguloInv(n):
    print(f"Dibujar un triangulo de {nFil} filas")
    linea = ""

    for f in range(n):
        for c in range(n-f):
            linea += "*"
        print(linea)
        linea = "" #vaciar la linea una vez impresa   

def trianguloReves(n):
    print(f"Dibujar un triangulo de {nFil} filas")
    linea = ""

    for f in range(n):
        """for c1 in range(n-f-1):
            linea += " "
        for c2 in range(f+1):
            linea += "*"
        
        print(linea)
        """
        linea = "" #vaciar la linea una vez impresa   

def trianguloRevesInv(n):
    print(f"Dibujar un triangulo de {nFil} filas")
    linea = ""

    for f in range(n):
        for c1 in range(f):
            linea += " "
        for c2 in range(n-f):
            linea += "*"
        
        print(linea)
        linea = "" #vaciar la linea una vez impresa 

match fig:
    case 1:
        cuadrado(nFil)
    case 2:
        triangulo(nFil)
    case 3:
        trianguloInv(nFil)
    case 4:
        trianguloReves(nFil)
    case 5:
        trianguloRevesInv(nFil)
    case _:
        print("Opcion no contemplada")





