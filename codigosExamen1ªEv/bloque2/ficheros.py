#!C:\Users\zx22student3208\AppData\Local\Programs\Python\Python311\python.exe
import cgi, os
import cgitb; cgitb.enable()
import csv

print("Content-Type: text/plain\n")

dir ="datos/"
nombreFich = "palabras.dat"

fich = open(dir+nombreFich) # Abrimos el fichero

listaDias = [dia.strip('\n') for dia in fich.readlines()] # Leemos el fichero y lo guardamos en una variable


if "Lunes" in listaDias:
    print("Esta el lunes")

#Bucle para leer linea a linea
while contenido:
    print("_"+contenido)
    contenido = fich.readline()
else:
    print("Fin de fichero")

#Bucle para leer linea a linea 2
for contenido in fich:
    print(contenido)

#Escribir en el fichero
try:
    fich=open(dir+nombreFich,"x")

    fich.write("\nPalabra")
except:
    print("Problemas al abrir el fichero")
    
fich.close

#--------------------------------

#!C:\Users\zx22student3208\AppData\Local\Programs\Python\Python311\python.exe

# <!DOCTYPE html>
# <html lang="en">
# <body>
#     <form action="tratarFichero.py" enctype="multipart/form-data" method="post">
#         <p>Fichero a subir <input type="file" name="filename"></p>
#         <p><input type="submit" value="Subir"></p>
#     </form>
# </body>
# </html>

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
