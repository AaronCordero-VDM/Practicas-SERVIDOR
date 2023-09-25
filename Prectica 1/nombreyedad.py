#!C:\Users\zx22student3208\AppData\Local\Programs\Python\Python311\python.exe

print("Content-type: text/html\n")

import os
from urllib.parse import urlparse, unquote, parse_qs

print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Tratar formulario</title>
</head>
<body>
      <h1>Tratar formulario</h1>
""")
      
ru = os.environ.get("REQUEST_URI") #guarda el request en la variable ru
parametros = urlparse(ru)
param = parse_qs(parametros[4])

print("Nombre: "+param['nombre'][0])
print("<br />")
print("Edad: "+param['edad'][0])

print("""
</body>
</html>
""")