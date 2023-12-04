#!C:\Users\zx22student3208\AppData\Local\Programs\Python\Python311\python.exe

import mysql.connector
import sys
import os
from urllib.parse import parse_qs

print("Content-type: text/html\n")

param = parse_qs(os.environ.get("QUERY_STRING"))


bdconx = mysql.connector.connect( 
            host="localhost",
            user="academia",
            password="academia",
            database="academia")

mi_cursor = bdconx.cursor()

if ("estudiante" in param and param["estudiante"][0] != "" \
    and "curso" in param and param["curso"][0] != "" \
    and "profesor" in param and param["profesor"][0] != ""):
        estudiante = param["estudiante"][0]
        curso = param["curso"][0]
        profesor = param["profesor"][0]
        consultaEstudiante = (f"SELECT id FROM estudiantes WHERE nombre = '{estudiante}'")
        mi_cursor.execute(consultaEstudiante)
        mi_resultado = mi_cursor.fetchone()
        consultaInsertarCurso = (f"INSERT INTO cursos(nombre_curso,profesor,id_estudiante) VALUES ({curso},{profesor},{mi_resultado})")
        mi_cursor.close()

else:
    print("Error")
