#!C:\Users\zx22student3208\AppData\Local\Programs\Python\Python311\python.exe

print("Content-Type: text/html\n")

import os
from urllib.parse import parse_qs
from math import sqrt

param = parse_qs(os.environ.get("QUERY_STRING"))

n1 = float(param["cateto1"][0])
n2 = float(param["cateto2"][0])


res = sqrt((n1*n1)+(n2*n2))



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
print("La hipotenusa de este triangulo es:\n {}".format("%.3f" % res))

print("""
      </h3>

    </body>
</html>
""")