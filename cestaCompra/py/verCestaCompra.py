#!C:\Users\zx22student3198\AppData\Local\Programs\Python\Python311\python.exe

import http.cookies, os
import funcionesHTML

numTeclados = 0
numMonitores = 0
numRatones = 0

print("Content-type: text/html\n")
cookie = http.cookies.SimpleCookie() 

if os.environ.get("HTTP_COOKIE") != None:
    cookie.load(os.environ.get("HTTP_COOKIE"))
    if "teclados" in cookie: #comprobar si la cookie teclados existe en cookies
        numTeclados = cookie["teclados"].value
    if "monitores" in cookie: #comprobar si la cookie montiores existe en cookies
        numMonitores = cookie["monitores"].value
    if "ratones" in cookie: #comprobar si la cookie ratones existe en cookies
        numRatones = cookie["ratones"].value



funcionesHTML.cabeceraHtml()

print("<p>Numero de teclados: "+numTeclados+"</p>")
print("<p>Numero de monitores: "+numMonitores+"</p>")
print("<p>Numero de ratones: "+numRatones+"</p>")


funcionesHTML.finHtml()