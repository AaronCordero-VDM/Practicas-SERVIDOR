#!C:\Users\zx22student3208\AppData\Local\Programs\Python\Python311\python.exe

import cgi, os
import cgitb; cgitb.enable()

form = cgi.FieldStorage()

print("Content-Type: text/html\n")

fileitem = form['filename']

#Comprobar si el archivo se a subido
if fileitem.filename:
    #guarda el nombre del archivo
    fn = os.path.basename(fileitem.filename)

    #Abrir el archivo u escribirlo en el servidor
    open("img/"+fn,"wb").write(fileitem.file.read())
    print("<img src='img/"+fn+"'>")