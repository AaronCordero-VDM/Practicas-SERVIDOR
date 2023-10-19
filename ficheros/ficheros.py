#!C:\Users\zx22student3208\AppData\Local\Programs\Python\Python311\python.exe

print("Content-Type: text/plain\n")

dir ="datos/"
nombreFich = "palabras.dat"

"""
fich = open(dir+nombreFich)


listaDias = [dia.strip('\n') for dia in fich.readlines()]


if "Lunes" in listaDias:
    print("Esta el lunes")

while contenido:
    print("_"+contenido)
    contenido = fich.readline()
else:
    print("Fin de fichero")


for contenido in fich:
    print(contenido)
"""
try:
    fich=open(dir+nombreFich,"x")

    fich.write("\nPalabra")
except:
    print("Problemas al abrir el fichero")
    
fich.close