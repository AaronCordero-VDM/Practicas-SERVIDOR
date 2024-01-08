#!C:\Users\zx22student3208\AppData\Local\Programs\Python\Python311\python.exe

import json

equipos = [
        "Real Madrid",
        "Barcelona",
        "Atlético de Madrid",
        "Sevilla",
        "Valencia"
    ]

equipos_liga = {"equipos": equipos}

equipos_json = json.dumps(equipos_liga, indent=2)

print("Content-Type: application/json\n")

print(equipos_json)

