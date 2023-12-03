#!C:\Users\zx22student3206\AppData\Local\Programs\Python\Python311\python.exe

from urllib.parse import parse_qs
import os

# Obtener los parametros que envía el formulario
parameter = parse_qs(os.environ.get('QUERY_STRING'))

if "precio_corte" not in parameter or parameter["precio_corte"][0] == "": # Comprueba que el input del formulario se haya pasado correctamente, si no es así, muestra un error y te devuelve al formulario
    print("""
    <html>
        <head>
            <meta http-equiv="refresh" content="2;formulario.html"/>
        </head>
        <body>
            <h1>Rellena los campos</h1>
        </body>
    </html>
    """)
    exit()

precio_corte = float(parameter["precio_corte"][0])
productos = []
precios_string = []
precios = []

with open("productos.txt","r") as file: # Abre el fichero en modo lectura, lo lee, separa la lina por los espacios y guarda los nombres de los productos en un array
    productos = file.read().split(" ")

with open("precios.txt", "r") as file: # Abre el fichero en modo lectura, lo lee, separa la lina por los espacios y guarda los precios de los productos en un array
    precios_string = file.read().split(" ")

for valor in precios_string: # Convierte el array de precios de string a float
    precios.append(float(valor))

productos_filtrados = ""
for i in range(len(precios)): # Por cada iteracion que se pueda hacer en la lista precios
    if precio_corte <= precios[i]: # Si el precio de corte pasado en el formulario es menor o igual al precio del producto, se apunta el producto
        productos_filtrados += f"{productos[i]} "

with open("productos_filtrados.txt","wt") as file: # Escribe el listado de los productos que sobrepasan el precio de corte
    file.write(productos_filtrados)

print("Content-type: text/html\n")
print("""
    <html>
        <head/>
        <body>
            <h1>Filtrado realizado</h1>
        </body>
    </html>
    """)