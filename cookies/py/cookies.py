#!C:\Users\zx22student3208\AppData\Local\Programs\Python\Python311\python.exe

import os, http.cookies
from urllib.parse import parse_qs

param = parse_qs(os.environ.get("QUERY_STRING"))

usuario = (param["usuario"][0])
passwd = (param["passwd"][0])
dentro = False

if (usuario == "pepe") and (passwd == "1234"):
    dentro = True

if not dentro:
    print("Content-Type: text/html\n")
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
        <h1>Cookies</h1>
          <h3>ERROR EN LA AUTENTICACION</h3>
        <form action="py/cookies.py" method="get" class="was-validated">
            <label for="usuario">Usuario</label>
            <input type="text" name="usuario" id="usuario"><br />
            <label for="contraseña">Contraseña</label>
            <input type="text" name="contraseña" id="contraseña"><br />
            <button type="submit" class="rounded-2 bg-dark-subtle">Entrar</button>
        </form>
    </body>

    </html>
    """)
else:
    print("Content-Type: text/html")
    cookie = http.cookies.SimpleCookie()
    cookie["ID1"] = "Algo"

    print(cookie)
    print()
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
        <h1>Estas dentro</h1>
    </body>
    </html>
    """)