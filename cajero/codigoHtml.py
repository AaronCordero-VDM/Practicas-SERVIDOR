
def pagPrincipal():
    print("""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Pagina Principal</title>
            <link rel="stylesheet" href="css/style.css">
            </head>
        <body>
            <h1>BBVA</h1>
    """)


def finHtml():      
    print("""
        </body>
        </html>
    """)

def listarCuentasInicio():
    print("""
    <h2>Tus cuentas:</h2>
    <div class='tabla'>
    
    """)

def listarCuentasFin():
    print("""
          </table>
          </div>
          <br>
    <div class='forms'>
    <form action="nuevaCuenta.py" method="get">
          <button type="submit">Crear cuenta</button>   
    </form>
    </div>
          <hr>
""")
    
def operacionesInicio():
    print("""
        <form action="operaciones.py" method="get">
        <h2>Operacion</h2>
        <div class='tabla2'>
          <br>
          <table>
            <tr><td for="cuenta">Cuenta:</td>
            <td><select name="cuenta">
            <option>Ninguna</option>
    """)
    


def operacionesFin():
    print("""
            </select>
            </td>
            </tr>
            <tr><td for="cantidad">Cantidad:</td>
            <td><input type="number" name="cantidad" id="cantidad" step="5" value="0"/></td>
            </tr>
            <tr><td for="concepto">Concepto:</td>
            <td><input required type="text" name="concepto" id="concepto" value="Varios" placeholder="Introduce el concepto"/></td>
            </tr>
            </table>
        </div>
          <hr>
        <div class="metodo">
          <br>
            <input type="radio" id="ingresar" variable=v name="operacion" value="ingresar" checked/>
            <label for="ingresar" class='ingresar'>Ingresar</label>
            <br>
            <input type="radio" id="retirar" variable=v name="operacion" value="retirar" />
            <label for="retirar" class='retirar'>Retirar</label>
            <br>
          </div>
          <div class="boton">
          <button>Confirmar</button>
          </div>
        
    
    </form>
          """)

    
def recarga():
    print("""
        <!DOCTYPE html>
        <html lang="en">

        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <meta http-equiv="refresh" content="2;pagPrincipal.py">
            <link rel="stylesheet" href="css/style.css">
            </head>

        <body>
          <div class="loading">
            <h1 class="textoLoad">Realizando operacion</h1>
            <h3 class="textoLoad">Espere un segundo</h3>
          </div>
          <div class="loader">
          <div class="lds-facebook"><div></div><div></div><div></div></div>
          </div>
        </body>
        </html>
    """)

def recargaSinCambios():
    print("""
        <!DOCTYPE html>
        <html lang="en">

        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <meta http-equiv="refresh" content="2;pagPrincipal.py">
            </head>

        <body>
        </body>
        </html>
    """)
