#!C:\Users\zx22student3208\AppData\Local\Programs\Python\Python311\python.exe

print("Content-type: text/html\n")

import sys
import os
from urllib.parse import parse_qs

#   7. FILTRAR 
def crearFiltros():
    #   Recuperar datos desde html para poder guardarlos en variables
    param = parse_qs(os.environ.get("QUERY_STRING"))

    filtro=""

    # Comprobar que existe empresa en la url y que no esta vacia
    if "empresa" in param and param["empresa"][0] != "":
        empresa = param["empresa"][0]
        filtro += f"empresa = '{empresa}'"
    
    if "tematica" in param and param["tematica"][0] != "":
        # Añadir empresa y plataforma en el mismo filtro 
        if filtro != "":
            filtro += "AND "
        # sino lo dejo como está    
        tematica = param["tematica"][0]
        filtro += f"tematica = '{tematica}'"

    if "numero_de_jugadores" in param and param["numero_de_jugadores"][0] != "":
        # Añadir empresa y plataforma en el mismo filtro 
        if filtro != "":
            filtro += "AND "
        # sino lo dejo como está    
        numero_de_jugadores = param["numero_de_jugadores"][0]
        filtro += f"numero_de_jugadores = '{numero_de_jugadores}'"


    if "anioInicial" in param and param["anioInicial"][0] != "":
        # Añadir empresa y plataforma en el mismo filtro 
        if filtro != "":
            filtro += "AND "
        # sino lo dejo como está    
        anioInicial = param["anioInicial"][0]
        filtro += f"publicacion >= '{anioInicial}'"

    if "anioFinal" in param and param["anioFinal"][0] != "":
        # Añadir empresa y plataforma en el mismo filtro 
        if filtro != "":
            filtro += "AND "
        # sino lo dejo como está    
        anioFinal = param["anioFinal"][0]
        filtro += f"publicacion <= '{anioFinal}'"

    sys.stderr.write(filtro)

    #   Si hay filtro, añadimos el where a la consulta
    if filtro != "":
        filtro = "WHERE " + filtro
       

    return filtro