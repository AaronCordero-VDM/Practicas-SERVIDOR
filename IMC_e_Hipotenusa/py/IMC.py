#!C:\Users\zx22student3208\AppData\Local\Programs\Python\Python311\python.exe

print("Content-Type: text/html\n")

import os
from urllib.parse import parse_qs

param = parse_qs(os.environ.get("QUERY_STRING"))

n1 = float(param["peso"][0])
n2 = float(param["altura"][0])

res = (n1 / (n2*n2))




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
      
      <div style="background-color: #9E8661; width: 80%; margin:3em 8em; text-align: center; border-radius: 15px ">
      <h1 style="color: white; ">Resultado</h1>
      <p style="color: white; font-size: 52px; padding: 20px ">
""")

print("Tu IMC es de \n {}".format("%.3f" % res))

print("""
      </p>
      </div>
    </body>
</html>
""")