#!C:\Users\zx22student3208\AppData\Local\Programs\Python\Python311\python.exe

print("Content-Type: text/html\n")

import os
from urllib.parse import parse_qs
from math import sqrt

param = parse_qs(os.environ.get("QUERY_STRING"))

texto = param["texto"][0]
palabra = param["palabra"][0]

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
finHtml()