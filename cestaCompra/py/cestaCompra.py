#!C:\Users\zx22student3198\AppData\Local\Programs\Python\Python311\python.exe

import http.cookies, os
import funcionesHTML


#   Comprobar si vienen productos para meter en la cesta
from urllib.parse import parse_qs
#   recuperar datos desde html para poder guardarlos en variables
param = parse_qs(os.environ.get("QUERY_STRING"))

#   variable que contiene el producto seleccionado, 0 es que no hya producto
prod = "0"

if "prod" in param:
    prod = param["prod"][0] # si viene algo sera el producto seleccionado, pos 0 



print("Content-type: text/html")
#   Forma de enviar la cookie al cliente 
cookie = http.cookies.SimpleCookie() 

# SI NO EXISTE LA COOKIE, LA CREO Y SE LA MANDO
if os.environ.get("HTTP_COOKIE") == None:
    cookie["teclados"] = 0
    cookie["monitores"] = 0
    cookie["ratones"] = 0

    cookie["teclados"]["expires"] = "Wed, 11 Oct 2024 07:28:00 GMT;" #cuando desaparecerá la cookie
    cookie["monitores"]["expires"] = "Wed, 11 Oct 2024 07:28:00 GMT;" 
    cookie["ratones"]["expires"] = "Wed, 11 Oct 2024 07:28:00 GMT;"
    print(cookie)
    print()
else:
    cookie.load(os.environ.get("HTTP_COOKIE"))
    if "teclados" in cookie: #comprobar si la cookie contador existe en cookies
        if prod == "1":
            cookie["teclados"] = int(cookie["teclados"].value) + 1 # incrementar si tengo la cookie teclados
    else:
        if prod == "1":
            cookie["teclados"] = 1
        else:
            cookie["teclados"] = 0 # si no tengo la cookie teclados, la pongo en 0
    cookie["teclados"]["expires"] = "Wed, 11 Oct 2024 07:28:00 GMT;" #siempre le creo fecha de extincion, por eso esta fuera del if
   

    if "monitores" in cookie:
        if prod == "2":
            cookie["monitores"] = int(cookie["monitores"].value) + 1
    else:
        if prod == "2":
            cookie["monitores"] = 1
        else:
            cookie["monitores"] = 0
    cookie["monitores"]["expires"] = "Wed, 11 Oct 2024 07:28:00 GMT;" 
        

    if "ratones" in cookie: 
        if prod == "3":
            cookie["ratones"] = int(cookie["ratones"].value) + 1
    else:
        if prod == "3":
            cookie["ratones"] = 1
        else:
            cookie["ratones"] = 0
    cookie["ratones"]["expires"] = "Wed, 11 Oct 2024 07:28:00 GMT;" 

    print(cookie)
    print()





funcionesHTML.cabeceraHtml()

print("<p>"+prod+"</p>") #control de parametro, a ver si entra correcto

print('<div id="contenedorImagenes">')
print('<a href="./cestaCompra.py?prod=1"><img class="imgTeclado" src="../imagenes/teclado.jpg"></a>')
print('<a href="./cestaCompra.py?prod=2"><img class="imgRaton" src="../imagenes/raton.jpg"></a>')
print('<a href="./cestaCompra.py?prod=3"><img class="imgMonitor" src="../imagenes/monitor.jpg"></a>')
print('<br />')
print('<a href="verCestaCompra.py">Ver carro</a>')
print("</div>")

funcionesHTML.finHtml()