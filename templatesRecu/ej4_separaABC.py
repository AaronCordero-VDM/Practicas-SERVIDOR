#!C:\Users\zx22student3206\AppData\Local\Programs\Python\Python311\python.exe

# Este python crea la cookie empiezaABC si no está y le asigna un valor, si existe ya, sólo añade el nuevo valor

from urllib.parse import parse_qs
import os
import http.cookies

# Obtener los parametros que envía el formulario
parameter = parse_qs(os.environ.get('QUERY_STRING'))

if "texto" in parameter and parameter["texto"][0] != "": # Comprueba que el input del formulario se haya pasado correctamente
    texto = parameter["texto"][0].strip(" ")
    if texto[0:3] == "ABC": # Compueba que el texto del input empiece por ABC, si es así crea/actualiza la cookie
        cookie = http.cookies.SimpleCookie()
        if os.environ.get("HTTP_COOKIE") is not None: # Si existen cookies ya creadas, las carga
            cookie.load(os.environ.get("HTTP_COOKIE"))
            if "empiezaABC" in cookie: # Si la cookie empiezaABC está creada, le añade el nuevo valor
                cookie["empiezaABC"] = str(cookie["empiezaABC"].value) + f" {texto[3:]}"
            else: # Si la cookie empiezaABC no está creada, la crea con el nuevo valor
                cookie["empiezaABC"] = str(f"{texto[3:]}")
        else: # Si no existen cookies ya creadas, crea la cookie empiezaABC con el nuevo valor
            cookie["empiezaABC"] = str(f"{texto[3:]}")
        print("Content-type: text/html") # Imprime la cabecera html necesaria para la cookie
        print(cookie) # Imprime la cookie
        print() # Imprime una linea en blanco
else: # Si no se han pasado los parametros correctamente, genera una cabecera para poder refrescar la página
    print("Content-type: text/html\n")

# Refresca la página
print("""
<html>
    <head>
        <meta http-equiv="refresh" content="0;formulario.html"/>
    </head>
</html>
""")