#!C:\Users\zx22student3208\AppData\Local\Programs\Python\Python311\python.exe

#Ejercicio 1, crear enlaces para las distintas redes sociales

print("Content-type: text/html\n")

redes_sociales=[("Twitter", "https://twitter.com/ejemplo_usuario"),
("Facebook","https://facebook.com/ejemplo_usuario"),
("Instagram","https://instagram.com/ejemplo_usuario"),
("LinkedIn","https://linkedin.com/in/ejemplo_usuario"),
("YouTube","https://youtube.com/c/ejemplo_usuario")]

# Imprimimos el comienzo del html
print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Tratar formulario</title>
</head>
<body>
      <h1>Redes Sociales</h1>
      <ul>
""")

# inicializamos un contador para agregar el id a las <li>
cont = 0;
# hacemos un bucla para recorrer la lista de tuplas de las redes
for red in redes_sociales:
    # icrementamos el contador
    cont+=1
    # imprimimos la li perteneciente a la red_social con el id correspondiente al contador
    # y su enlace con el enlace de la posicion 1 de la red y la 0 como el nombre
    print(f"<li id=red{cont}'><a href='{red[1]}'>{red[0]}</a></li>")
    
# Imprimimos el final del html
print("""
      </ul>
</body>
</html>
""")