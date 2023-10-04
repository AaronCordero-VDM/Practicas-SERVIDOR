#!C:\Users\zx22student3208\AppData\Local\Programs\Python\Python311\python.exe

print("Content-Type: text/html\n")

import os
from urllib.parse import parse_qs
from math import sqrt

param = parse_qs(os.environ.get("QUERY_STRING"))

texto = param["texto"][0]
palabra = param["palabra"][0]
letra = param["letra"][0]

#Funciones apoyo
def inicioHtml(): #devuelve el inicio del HTML
    print("""
    <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Calculadora</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet">
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/js/bootstrap.bundle.min.js"></script>
    </head>

    <body>
        <div style="background-color: #9E8661; width: 80%; margin:3em 5em; text-align: center; border-radius: 15px ">
            <h2 style="color: white; ">Resultado</h2>
                <p style="color: white; font-size: 22px; padding: 20px ">
    """)

def finHtml(): #devuelve el final del HTML
    print("""
                </p>
            </div>
        </body>
    </html>
    """)

#Funcion para separar las letras de texto
def separaLetras(texto):
    for letra in texto:
        print(letra + "<br/>")

#Funcion para contar las letras de una palabra
def contarLetras(texto):
    contador = 0
    for l in texto:
        if l >= "A" and l <= "Z" or l == "Ñ":
            contador += 1
        if l >= "a" and l <= "z" or l == "ñ":
            contador += 1
        if l >= "á" and l <= "ü":
            contador += 1 
    print(contador)

#Da la vuelta a una cadena de caracteres, poniendo desde donde quieres que empiece hasta donde acaba pero en negativo
def letrasAlReves(texto):
    print(texto[:-20:-1])

def buscarPalabra(texto, palabra):
    encontrada = False
    if texto.find(palabra) != -1:
        encontrada = True
    return encontrada

#Buscamos una letra en una cadena de caracteres y cada vez que esta se encuentre se suma a un contador para sacar
# el total de veces que aparece la letra
def numeroLetra(texto, letra):
    contador = 0
    if len(letra) == 1:
        for l in texto.upper():
            if letra.upper() == l:
                contador += 1        
    else:    
        contador = -1
    return contador

#contamos la cantidad de cada vocal que aparece en el texto introducido
def contarVocales(texto):
    contadorA = 0
    contadorE = 0
    contadorI = 0
    contadorO = 0
    contadorU = 0
    for l in texto.upper():

        """
        if l == "A":
            contadorA += 1
        elif l == "E":
            contadorE += 1
        elif l == "I":
            contadorI += 1
        elif l == "O":
            contadorO += 1
        elif l == "U":
            contadorU += 1
        """

        match l.lower():
            case "a":
                contadorA += 1
            case "e":
                contadorE += 1
            case "i":
                contadorI += 1
            case "o":
                contadorO += 1
            case "u":
                contadorU += 1

    print("Hay: <br/> {} 'A'<br/> {} 'E' <br/> {} 'I' <br/> {} 'O' <br/> {} 'U'".format(contadorA,contadorE,contadorI,contadorO,contadorU))


def dividirFrase(texto):
   dividido = texto.split(" ")
   print(dividido)
   print("<br/>")
   for parte in dividido:
       print(parte + "<br/>")

#Salida enviada al cliente
inicioHtml()
print("<hr/>")
separaLetras(texto)
print("<hr/>")
contarLetras(texto)
print("<hr/>")
letrasAlReves(texto)
print("<hr/>")
if buscarPalabra(texto,palabra):
    print("Palabra encontrada")
else:
    print("Palabra no encontrada")
print("<hr/>")
print(numeroLetra(texto, letra))
print("<hr/>")
contarVocales(texto)
print("<hr/>")
dividirFrase(texto)
finHtml()