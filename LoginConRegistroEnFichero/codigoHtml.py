def error(texto):
    print("""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="stylesheet" href="css/style.css">
            <title>Login con registro</title>
            </head>
        <body>
            <h1>Error</h1>
    """)
    print(texto)
    print("""
        </body>
        </html>
    """)

def correcto():
    print("""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="stylesheet" href="css/style.css">
            <title>Login con registro</title>
            </head>
        <body>
            <h1>Correcto</h1>
        </body>
        </html>
    """)

def application(texto, enlace):
    print("""Content-Type: text/html\n
          
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="stylesheet" href="css/style.css">
            <title>Login con registro</title>
            </head>
        <body>
            <h1>Aceros de Hispania</h1>
            <h3>"""+texto+"""</h3>
          <a href="""+enlace+""">enlace a la otra pagina</a>
          <br>
        <a href="logout.py">Salir de la aplicacion</a>
        </body>
        </html>
    """)

