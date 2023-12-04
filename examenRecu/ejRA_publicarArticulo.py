#!C:\Users\zx22student3208\AppData\Local\Programs\Python\Python311\python.exe

import mysql.connector
from urllib.parse import parse_qs
import os, sys

print("Content-type: text/html\n")

def mensaje(message):
    print(f"""
    <html>
        <head>
            <meta http-equiv="refresh" content="2;form6.html"/>
        </head>
        <body>
            <h1>{message}</h1>
        </body>
    </html>
    """)

def get_categoria(categoria): # Obtiene todos los datos de la categoria y lo devuelve
    cursor = db_conect.cursor()
    consulta = "SELECT id FROM categorias WHERE nombre=%s"
    sys.stderr.write(consulta+"\n")
    cursor.execute(consulta,[categoria])
    resultado = cursor.fetchone()
    cursor.close()
    return resultado

def insert_articulo(data_list): # Inscribe el articulo que se le pase dentro del array en la categoria que se le pase en el array
    cursor = db_conect.cursor()
    consulta = "INSERT INTO articulos (titulo, contenido, id_categoria) VALUES (%s, %s, %s)"
    sys.stderr.write(consulta+"\n")
    sys.stderr.write(str(data_list)+"\n")
    cursor.execute(consulta,data_list)
    db_conect.commit()
    cursor.close()
    mensaje("Articulo publicado")

# Obtener los parametros que envía el formulario
param = parse_qs(os.environ.get('QUERY_STRING'))

if "titulo" not in param or "contenido" not in param or "categoria" not in param: # Comprueba la validez de los inputs
    mensaje("Rellena los campos")
    exit()

titulo = param["titulo"][0]
contenido = param["contenido"][0]
categoria = param["categoria"][0]

if titulo == "" or contenido == "" or categoria == "":
    mensaje("Rellena los campos")
    exit()

# Conectamos con la base de datos
db_conect = mysql.connector.connect(host="localhost",user="periodico",password="periodico",database="periodico")

# seleccionamos la categoria que queremos y ese id
id_categoria = get_categoria(categoria)

if not id_categoria != None: # comprueba que la categoria exista
    mensaje("La categoria no existe")
    exit()

# Creamos un array con los parametros necesarios par ala consulta
data = [titulo, contenido, id_categoria[0]]
# llamamos a la funcion para inserter el articulo en la base de datos
insert_articulo(data)

# Cerramos la conexion con la base de datos
db_conect.close()