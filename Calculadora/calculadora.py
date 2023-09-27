#!C:\Users\zx22student3208\AppData\Local\Programs\Python\Python311\python.exe

print("Content-Type: text/html\n")

import os
from urllib.parse import urlparse, unquote, parse_qs

ru = os.environ.get("REQUEST_URI")
parametros = urlparse(ru)
param = parse_qs(parametros[4])

# Asignamos a variables el valor de los imputs del HTML ["nombre"][]
n1 = float(param["num1"][0])
n2 = float(param["num2"][0])
oper = param["operacion"][0]






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
      <h1>Resultado</h1>
      <h3>
""")

if oper == "s":
    print("El resultado de sumar {} mas {} es: {}".format(n1,n2,(n1 + n2)))
if oper == "r":
    print(n1 - n2)
if oper == "m":
    print(n1 * n2)
if oper == "d":
    print(n1 / n2)
print("""
      </h3>
    </body>
</html>
""")

