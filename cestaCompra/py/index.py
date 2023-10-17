#!C:\Users\Kras\AppData\Local\Programs\Python\Python311\python.exe

import http.cookies, os

from urllib.parse import parse_qs

param = parse_qs(os.environ.get("QUERY_STRING"))

teclado = param["teclado"][0]
monitor = param["monitor"][0]
raton = param["raton"][0]

dentro = False

print("Content-type: text/html")
cookie = http.cookies.SimpleCookie()

if teclado == 0:
    cookie["TECLADO"] = 1
    cookie["TECLADO"]["expires"] = "Wed, 11 Oct 2024 07:28:00 GMT;" #cuando desaparecerá la cookie
    print(cookie)
    print()

if monitor == 0:
    cookie["MONITOR"] = 1
    cookie["MONITOR"]["expires"] = "Wed, 11 Oct 2024 07:28:00 GMT;" #cuando desaparecerá la cookie
    print(cookie)
    print()   

if raton == 0:
    cookie["RATON"] = 1
    cookie["RATON"]["expires"] = "Wed, 11 Oct 2024 07:28:00 GMT;" #cuando desaparecerá la cookie
    print(cookie)
    print()  

def htmlInicio():
    print("""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Contador de productos en el carrito</title>
        </head>
        <body>
            <h1>Carrito de Compra</h1>
    """)

def htmlFinal():
    print("""
        </body>
        </html>
    """)


"""
# SI NO EXISTE LA COOKIE, LA CREO Y SE LA MANDO
if os.environ.get("HTTP_COOKIE") == None:
    cookie["MONITOR"] = 1
    cookie["MONITOR"]["expires"] = "Wed, 11 Oct 2024 07:28:00 GMT;" #cuando desaparecerá la cookie
    print(cookie)
    print()
else:
    cookie.load(os.environ.get("HTTP_COOKIE"))
    if "MONITOR" in cookie: #comprobar si la cookie contador existe en cookies
        cookie["MONITOR"] = int(cookie["CONTADOR"].value) + 1
        cookie["MONITOR"]["expires"] = "Wed, 11 Oct 2024 07:28:00 GMT;" #  Al refrescar seguirá salinedo la fecha de desaparicion
        print(cookie)
        print()
    else:
        cookie["MONITOR"] = 1
        cookie["MONITOR"]["expires"] = "Wed, 11 Oct 2024 07:28:00 GMT;" #cuando desaparecerá la cookie
        print(cookie)
        print()

"""




# Código HTML que se envía al navegador
htmlInicio()
print("<h3>"+cookie["MONITOR"].value+"</h3>")

htmlFinal()
