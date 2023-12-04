#!C:\Users\zx22student3208\AppData\Local\Programs\Python\Python311\python.exe

import mysql.connector
from urllib.parse import parse_qs
import os, sys

print("Content-type: text/html\n")

def mensaje(mensaje):
    print(f"""
    <html>
        <head>
            <meta http-equiv="refresh" content="2;form6.html"/>
        </head>
        <body>
            <h1>{mensaje}</h1>
        </body>
    </html>
    """)

def idCategoria(categoria): # Obtiene la categoria y la devuele
    cursor = db_conect.cursor() # Crea un cursor
    consulta = "SELECT id FROM categorias WHERE nombre=%s"
    sys.stderr.write(consulta+"\n")
    cursor.execute(consulta,[categoria])
    resultado = cursor.fetchone()
    cursor.close() # Cierra el cursor
    return resultado # Devuelve los resultados de la consulta

def getArticulos(id_categoria):
    cursor = db_conect.cursor() # Crea un cursor
    consulta = "SELECT * FROM articulos WHERE id_categoria=%s" # Crea la consulta SQL
    sys.stderr.write(str(consulta)+"\n") # Escribe la consulta completa en el log de errores de apache
    cursor.execute(consulta,id_categoria) # Ejecuta la consulta SQL
    result = cursor.fetchall() # Guarda los resultados de la consulta SQL en una variable
    cursor.close() # Cierra el cursor
    return result # Devuelve los resultados de la consulta


    
# Obtener los parametros que envía el formulario
param = parse_qs(os.environ.get('QUERY_STRING'))

if "categoria" not in param: # Comprueba la validez de los inputs
    mensaje("Rellena los campos")
    exit()
categoria = param["categoria"][0]

if categoria == "":
    mensaje("Rellena los campos")
    exit()

# Conectamos con la base de datos
db_conect = mysql.connector.connect(host="localhost",user="periodico",password="periodico",database="periodico")

# Llamamos a la funcion para hacer la consulta a categorias y coger el id de la categoria seleccionada
id_categoria = idCategoria(categoria)

# LLamamos a la funcion para hacer la consulta a articulos y seleccionamos todos con la categoria seleccionasa
articulos = getArticulos(id_categoria)
lista = "<ul>"
# Recorremos con un bucle los articulos devueltos de la funcion
for art in articulos:
    # guardamos en una lista los distintos articulos
    lista += f"<li>Titulo: {art[1]} y contenido: {art[2]}</li>"
lista += "</ul>"

# Imprimimos la lista
print(f"""
<html>
    <head/>
    <body>
      <h1>Articulos</h1>
        {lista}
    </body>
</html>
""")

# Cerramos la conexion con la base de datos
db_conect.close()