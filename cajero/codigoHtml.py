
def pagPrincipal():
    print("""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Pagina Principal</title>
            </head>
        <body>
            <h1>Bienvenido</h1>
    """)
    

def finHtml():      
    print("""
        </body>
        </html>
    """)

def listarCuentasInicio():
    print("""
    <h2>Tus cuentas:</h2>
    """)

def listarCuentasFin():
    print("""
          <hr>  
    <form action="nuevaCuenta.py" method="get">
          <button type="submit">Crear cuenta</button>   
    </form>
          <hr>
""")
    
def operacionesInicio():
    print("""
    <form action="operaciones.py" method="get">
          <label for="cuenta">Cuenta a retirar:</label>
          <select name="cuenta">
    """)
    


def operacionesFin():
    print("""
          </select>
          <br>
          <br>
          <label for="cantidad">Cantidad a retirar:</label>
          <input type="number" name="cantidad" id="cantidad" step="5"/>
          <span>Euros</span>
          <br>
            <input type="radio" id="ingresar" variable=v name="operacion" value="ingresar" />
            <label for="ingresar">Ingresar</label>
            <input type="radio" id="retirar" variable=v name="operacion" value="retirar" />
            <label for="retirar">Retirar</label>
            <br>
          <button>Confirmar</button>
    </form>
    <hr>
          """)

    
def recarga():
    print("""
        <!DOCTYPE html>
        <html lang="en">

        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <meta http-equiv="refresh" content="2;pagPrincipal.py">
            </head>

        <body>
            <h1>Realizando operacion</h1>
            <h3>Espere un segundo</h3>
        </body>
        </html>
    """)
