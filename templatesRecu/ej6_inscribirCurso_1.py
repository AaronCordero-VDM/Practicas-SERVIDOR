#!C:\Users\zx22student3206\AppData\Local\Programs\Python\Python311\python.exe

# Este python permite inscribir a un estudiante en un curso

import mysql.connector
from urllib.parse import parse_qs
import os, sys

def message_page(message):
    print("Content-type: text/html\n")
    print(f"""
    <html>
        <head>
            <meta http-equiv="refresh" content="2;formulario.html"/>
        </head>
        <body>
            <h1>{message}</h1>
        </body>
    </html>
    """)

def get_estudiante(estudiante): # Obtiene todos los datos del estudiante que se le pase como parametro y lo devuelve
    cursor = database_connection.cursor()
    consulta = "SELECT id FROM estudiantes WHERE nombre=%s"
    sys.stderr.write(consulta+"\n")
    cursor.execute(consulta,[estudiante])
    resultado = cursor.fetchone()
    cursor.close()
    return resultado

def insert_curso(data_list): # Inscribe el usuario que se le pase dentro del array en el curso que se le pase en el array
    cursor = database_connection.cursor()
    consulta = "INSERT INTO cursos (nombre_curso, profesor, id_estudiante) VALUES (%s, %s, %s)"
    sys.stderr.write(consulta+"\n")
    sys.stderr.write(str(data_list)+"\n")
    cursor.execute(consulta,data_list)
    database_connection.commit()
    cursor.close()
    message_page("Estudiante inscrito")

# Obtener los parametros que envía el formulario
parameter = parse_qs(os.environ.get('QUERY_STRING'))

if "estudiante" not in parameter or "curso" not in parameter or "profesor" not in parameter: # Comprueba la validez de los inputs
    message_page("Rellena los campos")
    exit()

estudiante = parameter["estudiante"][0]
curso = parameter["curso"][0]
profesor = parameter["profesor"][0]

if estudiante == "" or curso == "" or profesor == "": # Comprueba la validez de los inputs
    message_page("Rellena los campos")
    exit()

database_connection = mysql.connector.connect(host="localhost",user="academia",password="academia",database="academia")

id_estudiante = get_estudiante(estudiante)

if not id_estudiante != None: # comprueba que el estudiante exista
    message_page("El estudiante no existe")
    exit()

data = [curso, profesor, id_estudiante[0]]
insert_curso(data)

database_connection.close()