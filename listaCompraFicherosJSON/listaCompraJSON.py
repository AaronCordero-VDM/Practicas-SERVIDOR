#!C:\Users\zx22student3208\AppData\Local\Programs\Python\Python311\python.exe

print("Content-Type: text/html\n")

#Importamos tanto el os como el otro archivo .py
import os,codigoHtml, json

#Intentamos abrir 
try:
   fich = open("datos/listaCompra.dat")
except:
   fich = open("datos/listaCompra.dat","x")

if os.path.getsize("datos/listaCompra.dat") != 0:
    productos = json.load(fich)
else:
    productos = []

def listaDeProductos():
    if len(productos) != 0:
        print("<ol>")
        for p in productos:
            print(f"<li>{p[1]} de {p[0]}</li>")
        print("</ol>")
    else:
        print("<h3>No hay productos en la cesta</h3>")
    print("<hr>")

fich.close()

(codigoHtml.cabeceraHtml())

listaDeProductos()

codigoHtml.formulario()

(codigoHtml.finHtml())
