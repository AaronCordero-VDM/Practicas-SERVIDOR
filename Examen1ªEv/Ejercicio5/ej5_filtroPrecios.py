#!C:\Users\zx22student3208\AppData\Local\Programs\Python\Python311\python.exe

print("Content-Type: text/html\n")

from urllib.parse import urlparse, parse_qs
import os

ru = os.environ.get("REQUEST_URI")
parametros = urlparse(ru)
param = parse_qs(parametros[4])

precioCorte = param["precio_corte"][0]

def listarProdFiltrados():
    prodFiltrados = open(prodFiltradosFich) # Abrimos el fichero productosFiltrados
    listaProdFiltrados = [prod.strip('\n') for prod in prodFiltrados.readline().split(";")]
    for prodFilt in listaProdFiltrados:
        print(prodFilt)

productosFich = "productos.txt"
preciosFich = "precios.txt"
prodFiltradosFich = "productos_filtrados.txt"

fichProd = open(productosFich) # Abrimos el fichero productos
fichPre = open(preciosFich) # Abrimos el fichero pecios

listaProd = [producto.strip('\n') for producto in fichProd.readline().split(" ")] # Leemos el fichero y lo guardamos en una variable
listaPre = [precio.strip('\n') for precio in fichPre.readline().split(" ")]

pos = 0
for precio in listaPre:
    if precio >= precioCorte:
        try:
            fich=open(prodFiltradosFich,"a")

            fich.write(listaProd[pos]+";")
            
        except:
            print("Problemas al abrir el fichero")
    pos += 1

listarProdFiltrados()


        
fichPre.close
fichProd.close