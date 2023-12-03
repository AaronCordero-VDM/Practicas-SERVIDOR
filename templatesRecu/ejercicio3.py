#!C:\Users\zx22student3206\AppData\Local\Programs\Python\Python311\python.exe

# Este python crea una tabla con los elementos de un diccionario y el total de los valores del mismo

print("Content-type: text/html\n")

preciosProductosID = {
    "CA132":99.2,
    "CB231":55.7,
    "CA332":101.0,
    "CD563":65.2,
    "CB838":48.1
}
total = 0

table = "<table border='1'><theader><tr><th>Identificador</th><th>Precio</th></tr></theader><tbody>"
for id, precio in preciosProductosID.items(): # Por cada elemento del array, crea un tr con dos td, uno que almacena la clave del elemento y otro que almacena el valor, también va sumando los valores para generar el total
    table += f"<tr><td>{id}</td><td>{precio}</td></tr>"
    total += precio
table += f"<tr><td>Total:</td><td>{total}</td></tr></tbody></table>" # Concatena el total en un tr

print(table)