#!C:\Users\zx22student3208\AppData\Local\Programs\Python\Python311\python.exe

import sys, json, mysql.connector

sys.stderr.write("Dentro del pedirdatos.py ------------- \n")

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
consulta = "SELECT * FROM datos"
#Ejecutar la consulta
miCursor.execute(consulta)
#Obtener las filas de la consulta y guardar en la variable
miResultado = miCursor.fetchall()

#Traza para ver el resultado
sys.stderr.write(str(miResultado))

#Cerrar cursor y conexion
miCursor.close()
miBD.close()


#Generar salida para el cliente ajax
print("Content-Type: application/json\n")

print(json.dumps(miResultado))

sys.stderr.write("Fin de pedirdatos.py")
