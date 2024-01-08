#!C:\Users\zx22student3208\AppData\Local\Programs\Python\Python311\python.exe

import json
import cgi

equipos = {
    "Real Madrid": {
        "ciudad": "Madrid",
        "estadio": "Santiago Bernabéu",
        "titulos": 34
    },
    "Barcelona": {
        "ciudad": "Barcelona",
        "estadio": "Camp Nou",
        "titulos": 26
    },
    "Atlético de Madrid": {
        "ciudad": "Madrid",
        "estadio": "Estadio Metropolitano",
        "titulos": 11
    },
    "Sevilla": {
        "ciudad": "Sevilla",
        "estadio": "Ramón Sánchez-Pizjuán",
        "titulos": 1
    },
    "Valencia": {
        "ciudad": "Valencia",
        "estadio": "Mestalla",
        "titulos": 6
    }
}

form = cgi.FieldStorage()

if 'equipo' in form:
    nombre_equipo = form.getvalue('equipo')
    datos_equipo = equipos[nombre_equipo]
else:
    print(json.dumps({"error": "Equipo no especificado"}, indent=4))


print("Content-Type: application/json\n")

print(json.dumps(datos_equipo, indent=4))
