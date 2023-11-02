#!C:\Users\zx22student3208\AppData\Local\Programs\Python\Python311\python.exe

import http.cookies

cookie = http.cookies.SimpleCookie()
cookie["Usuario"] = 1
cookie["Usuario"]["expires"] =  "Wed, 11 Oct 2022 07:28:00 GMT"

print("Content-Type: text/html")
print(cookie["Usuario"])
print()

print("""<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <meta http-equiv="refresh" content="2;index.html">
            <link rel="stylesheet" href="css/style.css">
            <title>Login con registro</title>
            </head>
        <body>
            <h1>Saliendo de la aplicacion</h1>
        </body>
        </html>
    """)