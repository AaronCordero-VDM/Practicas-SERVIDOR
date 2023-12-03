#!C:\Users\zx22student3206\AppData\Local\Programs\Python\Python311\python.exe

import mysql.connector
import os, sys

print("Content-type: text/html\n")

def fetch_all_estudiantes(): # Obtiene todos los estudiantes y los devuele
    cursor = database_connection.cursor() # Crea un cursor
    consulta = f"SELECT * FROM estudiantes" # Crea la consulta SQL
    sys.stderr.write(str(consulta)+"\n") # Escribe la consulta completa en el log de errores de apache
    cursor.execute(consulta) # Ejecuta la consulta SQL
    result = cursor.fetchall() # Guarda los resultados de la consulta SQL en una variable
    cursor.close() # Cierra el cursor
    return result # Devuelve los resultados de la consulta

def fetch_nombre_cursos(id_usuario):
    cursor = database_connection.cursor() # Crea un cursor
    consulta = "SELECT nombre_curso FROM cursos WHERE id_estudiante=%s" # Crea la consulta SQL
    sys.stderr.write(str(consulta)+"\n") # Escribe la consulta completa en el log de errores de apache
    cursor.execute(consulta,id_usuario) # Ejecuta la consulta SQL
    result = cursor.fetchall() # Guarda los resultados de la consulta SQL en una variable
    cursor.close() # Cierra el cursor
    return result # Devuelve los resultados de la consulta

database_connection = mysql.connector.connect(host="localhost",user="academia",password="academia",database="academia")

estudiantes = fetch_all_estudiantes()

lista = ""
for estudiante in estudiantes: # Crea la lista con los cursos
    lista += f"<h1>{estudiante[1]} se ha inscrito en:</h1><ul>"
    for curso in fetch_nombre_cursos([estudiante[0]]):
        lista += f"<li>{curso[0]}</li>"
    lista += "</ul>"

database_connection.close()

print(f"""
    <html>
        <head/>
        <body>
            {lista}
        </body>
    </html>
    """)