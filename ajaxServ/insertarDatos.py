#!C:\Users\zx22student3208\AppData\Local\Programs\Python\Python311\python.exe

import sys, json, mysql.connector
import os
from urllib.parse import urlparse, unquote, parse_qs

sys.stderr.write("Dentro del pedirdatos.py ------------- \n")

ru = os.environ.get("REQUEST_URI") #guarda el request en la variable ru
parametros = urlparse(ru)
param = parse_qs(parametros[4])

texto = param["texto"][0]
numero = param["numero"][0]

#Consuta a base de datos
miBD = mysql.connector.connect(
    host = "localhost",
    user = "pruebaAjax",
    password ="pruebaAjax",
    database = "pruebaAjax"
)

#Crear un cursor para hacer la sonsulta
miCursor = miBD.cursor()
#Crear la consulta
inserccion = f"INSERT INTO datos (dato1, dato2) VALUES ('{texto}', {numero})"
#Ejecutar la consulta
miCursor.execute(inserccion)
miBD.commit()
#Obtener las filas de la consulta y guardar en la variable

#Cerrar cursor y conexion
miCursor.close()
miBD.close()

#Generar salida para el cliente ajax
print("Content-Type: application/json\n")

print(json.dumps("ok"))

sys.stderr.write("Fin de pedirdatos.py")
