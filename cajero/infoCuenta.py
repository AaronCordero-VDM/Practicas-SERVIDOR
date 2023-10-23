#!C:\Users\zx22student3208\AppData\Local\Programs\Python\Python311\python.exe


print("Content-Type: text/html\n")

import os, codigoHtml, json
from urllib.parse import parse_qs
import requests

param = parse_qs(os.environ.get("QUERY_STRING"))

cuenta = (param["id"][0])

try:
   fich = open("datos/listaCuentas.dat")
except:
   fich = open("datos/listaCuentas.dat","x")

if os.path.getsize("datos/listaCuentas.dat") != 0:
    cuentas = json.load(fich)
else:
    cuentas = []

#Funcion para ver la informacion de la cuenta
def listarInformacion():
    #Bucle para recorrer todas las cuetnas
    for c in cuentas:
        #Si la cuenta conincide con la cuenta seleccionada
        if cuenta == c[1]:
            print(f"<h2>Numero de cuenta: {cuenta}<hr>El saldo es de {c[2]} euros</h2><hr>")
            print(f"<h2>Ultimos movimientos</h2>")
            #Si la cuenta contiene operaciones
            if len(c) > 3:
                #Creamos la tabla para listar las operaciones
                print("<div class='tabla3'><table><th>Operacion</th><th>Concepto</th><th>Valor</th>")
                #Bucle para recorrer todas las operaciones que van desde la posicon 3 de la cuenta
                for t in range(3,len(c)):
                        #Si la operacion empieza con mas
                        if c[t].startswith("+"):
                            #Hacemos un split con " "
                            concepto = c[t].split(" ")
                            #Creamos la fila de la operacion con sus datos en cada celda
                            print(f"<tr style='color: green'><td id='tipoOperacion' name='tipoOperacion'>Ingreso</td>")
                            print(f"<td id='concepto'>{concepto[1]}</td>")
                            print(f"<td id='valor'>{concepto[3]}</td></tr>")
                        elif c[t].startswith("-"):
                            concepto = c[t].split(" ")
                            print(f"<tr style='color: red'><td id='tipoOperacion' name='tipoOperacion'>Retirada</td>")
                            print(f"<td id='concepto'>{concepto[1]}</td>")
                            print(f"<td id='valor'>{concepto[3]}</td></tr>")
                print("</table></div>")
                #print("<form action='pagPrincipal.py' method='get'><button type='submit'>Volver</button></form>")  
            else:
                print("<h3 style='text-align: center'>No has hecho movimientos</h3>")
    #Boton para volver a la pagina principal    
    print("<div class='volver'><form action='pagPrincipal.py'>")
    print("<button>Volver</button>")
    print("</form></dvi>")
            
                    
                
codigoHtml.pagPrincipal()
listarInformacion()
codigoHtml.finHtml()
