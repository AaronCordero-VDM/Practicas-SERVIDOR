#!C:\Users\zx22student3208\AppData\Local\Programs\Python\Python311\python.exe

print("Content-Type: text/html\n")

#Imprimimos el comienzo del html
print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Ejercicio 3</title>
</head>
<body>
      <h1>Lista de productos</h1>
""")

#Variable diccionario de los productos
preciosProductosID = {"CA132":"99.2","CB231":"55.7","CA332":"101.0","CD563":"65.2","CB838":"48.1"}
#Imprimimos el comienzo de la table y la as primeras filas
print("<table><tr><th>Identificador</th><th>Precio</th></tr>")
#Variable de la suma de precios
suma = 0
#bucle para recorrer el diccionario
for producto in preciosProductosID:
    #Imprimimos la fila para cada producto
    print(f"<tr><td>{producto}</td><td>{producto}</td></tr>")
    suma += producto
#Imprimimos la ultima fila de la tabla con el total de la suma
print(f"<tr><td>Total</td><td>{suma}</td></tr>)")


#Imprimimos el final del html
print("""
</table>
</body>
</html>
""")