#!C:\Users\zx22student3208\AppData\Local\Programs\Python\Python311\python.exe

import cgi, os
import cgitb; cgitb.enable()
import csv

form = cgi.FieldStorage()

print("Content-Type: text/html\n")

fileitem = form['filename']

def crearTabla():
    with(open("ligafutbol.csv", newline='') as file):
        
        cabecera = csv.reader(file, delimiter=";")
        print("<table border='1' style='border-collapse: collapse;'>")
        cont = 0
        for row in cabecera:
            print("<tr>")
            for e in row:
                if cont == 0:
                    print("<th>"+e+"</th>")
                else:
                    print("<td>"+e+"</td>")
            print("</tr>")
            cont += 1
        print("</table>")

#Comprobar si el archivo se a subido
if fileitem.filename:
    #guarda el nombre del archivo
    fn = os.path.basename(fileitem.filename)
    #Abrir el archivo u escribirlo en el servidor
    open(fn,"wb").write(fileitem.file.read())

    crearTabla()

