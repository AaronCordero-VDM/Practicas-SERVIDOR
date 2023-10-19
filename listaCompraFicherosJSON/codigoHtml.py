def cabeceraHtml():
    print("""
        <!DOCTYPE html>
        <html lang="en">

        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Cesta de la compra</title>
            </head>

        <body>
            <h1>Cesta de la compra</h1>
    """)
    

def finHtml():      
    print("""
        </body>
        </html>
    """)

def formulario():
    print("""
    <form action="productoNuevoJSON.py" method="get">
          <label for="nombre">Nombre del producto:</label>
          <input type="text" name="producto"/>
          <br>
          <label for="cantidad">Cantidad del producto:</label>
          <input type="text" name="cantidad"/>
          <br>
          <button>Enviar</button>        
    </form>
          """)
    
def recarga():
    print("""
        <!DOCTYPE html>
        <html lang="en">

        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <meta http-equiv="refresh" content="3;listaCompraJSON.py">
            <title>Cesta de la compra</title>
            <link rel="stylesheet" href="../css/style.css">
            </head>

        <body>
            <h1>Cesta de la compra</h1>
            <h3>Producto nuevo completados</h3>
        </body>
        </html>
    """)
    