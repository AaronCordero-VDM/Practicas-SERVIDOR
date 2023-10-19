#!C:\Users\zx22student3208\AppData\Local\Programs\Python\Python311\python.exe

print("Content-Type: text/html\n")

#Importamos tanto el os como el otro archivo .py
import os,codigoHtml

#Intentamos abrir 
try:
   fich = open("datos/listaCompra.dat")
except:
   fich = open("datos/listaCompra.dat","x")

if os.path.getsize("datos/listaCompra.dat") != 0:
    productos = fich.readlines()
else:
    productos = []

def listaDeProductos():
    if len(productos) != 0:
        print("<ol>")
        for p in [p.strip('\n') for p in productos]:
            elem = p.split(";")
            print(f"<li>{elem[1]} de {elem[0]}</li>")
        print("</ol>")
    else:
        print("<h3>No hay productos en la cesta</h3>")
    print("<hr>")

fich.close

(codigoHtml.cabeceraHtml())

listaDeProductos()

codigoHtml.formulario()

(codigoHtml.finHtml())
