#!C:\Users\zx22student3208\AppData\Local\Programs\Python\Python311\python.exe

#Ejercicio 3, lista en una tabla con las 3 propiedades del producto

print("Content-type: text/html\n")

print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Tabla produco</title>
</head>
<body>
      <h1>Productos</h1>
""")

inventarioProductos = {
    "PRD001": ("Laptop", 1200.00),
    "PRD002": ("Smartphone", 800.00),
    "PRD003": ("Tablet", 400.00),
    "PRD004": ("Monitor", 300.00),
    "PRD005": ("Teclado", 50.00)
}

# inicializamos el total del precio de los productos a 0
total = 0

# creamos la cabecera de la tabla con sus tittles
table = "<table border='1'><theader><tr><th>Identificador</th><th>Producto</th><th>Precio</th></tr></theader><tbody>"
# Bucle para recorrer el diccionario
for id, producto in inventarioProductos.items(): # Por cada elemento del diccionario, crea un tr con tres td, 
    # uno que almacena la clave del elemento, otro que almacena el tipo de producto y otro que almacena el valor, 
    table += f"<tr><td>{id}</td><td>{producto[0]}</td><td>{producto[1]}</td></tr>"
    # sumamos el precio del producto al total del precio
    total += producto[1]
# añadimos la ultima fila de la tabla con el total de la cantidad
table += f"<tr><td>Total:</td><td></td><td>{total}</td></tr></tbody></table>" # Concatena el total en un tr
# imprimimos la tabla
print(table)

print("""
</body>
</html>
""")