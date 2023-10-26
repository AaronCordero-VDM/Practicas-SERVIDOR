#!C:\Users\zx22student3208\AppData\Local\Programs\Python\Python311\python.exe

print("Content-Type: text/html")

import os
import codigoHtml
import json
import hashlib

from urllib.parse import parse_qs

param = parse_qs(os.environ.get("QUERY_STRING"))

fichUsu = "usuarios.json"

# Validar que nos envian los parametros
#         que existan
#         que contiene algo
#         que cumplen los requisitos, por ejermplo: la psswd sea de mas de 4 caracteres
    
#     El objetivo es guardar el nuevo usuario en el fichero usuarios

#     1-Abrir fichero usuarios.json 
#     2-Comprobar que el usuario no existe
#     3-Si no existe se añadir al fichero usuarios.json
#     4-Volver a la pagina principal
#     5-Si existe, ir a la pagina error

#     Formato de la estructura de datos par ala lista de usuario
#     Listas:
#         [["usuario","contraseña","correo"],["usuario","contraseña","correo"],[.append(nuevoUsuario)]]

def validarParametros():
    #condiciones
    #comprobar que vienen todos los parametros
    if "nombre" not in param:
        #le pasamos el mensaje al html donde pone texto
        codigoHtml.error("Falta el nombre")
        exit() # sale del python(de la ejecucion)
    if "password" not in param:
        #le pasamos el mensaje al html donde pone texto
        codigoHtml.error("Falta la contraseña")
        exit() # sale del python(de la ejecucion)
    if "email" not in param:
        #le pasamos el mensaje al html donde pone texto
        codigoHtml.error("Falta el correo")
        exit() # sale del python(de la ejecucion)

    nombre = param["nombre"][0]
    contraseña = param["password"][0]
    correo = param["email"][0]
    
    if nombre == "":
        #le pasamos el mensaje al html donde pone texto
        codigoHtml.error("El nombre tiene que tener algo")
        exit() # sale del python(de la ejecucion)
    if contraseña == "" or len(contraseña) < 5:
        #le pasamos el mensaje al html donde pone texto
        codigoHtml.error("Error en la contraseña, minimo 5 caracteres")
        exit() # sale del python(de la ejecucion)
    if correo == "" or correo.count('@') != 1:
        #le pasamos el mensaje al html donde pone texto
        codigoHtml.error("El correo tiene que tener algo o tiene que tener formato de email")
        exit() # sale del python(de la ejecucion)
        #asi devuelve una tupla ()
            #retureturn nombre, contraseña, correo
        #asi devuelve una lista []
    contraseñaEncriptada = (hashlib.sha512(str.encode(contraseña)).hexdigest())
    return [nombre, contraseñaEncriptada, correo]

def comprobarFichero():

    try:
        #abrir el fichero en modo lectura
        fich = open(fichUsu, "at")
    except:
        #Se crea el fichero si da error al abrir(si no existe)
        fich = open(fichUsu, "x")

    #leemos el contenido del fochero en una lista de productos si no esta vacio
    if os.path.getsize(fichUsu) == 0:
        fich.write("[]")
    #cerrar el fichero
    fich.close

#llamada a funcion(guarda los parametros del usuario a registrar) y la guardamos en una variable
usuario = validarParametros()

#comprobamos el estado del fichero(si existe y si no lo creamos)
comprobarFichero()

#funcion que que obtiene los usuarios registrados del fichero
#abrir, leer y cerrar fichero
#si da error te crea la lista vacia
with open(fichUsu) as fichero:
    try:
        #convierto el fichero json a una lista
        listaUsuarios = json.load(fichero)
    except:
        #crea la lista vacia
        listaUsuarios = []


#variable booleana
usuarioEncontrado = False

#te recorre la lista de usuarios y te guarda cada parametro en la variable
for usu in listaUsuarios:
    #si el aparametro guardado en la variable coincide con el nombre de la lista
    if(usu[0] == usuario[0]):
        #el usuario ya existe
        usuarioEncontrado = True
        break

if not usuarioEncontrado:
    #añado usuario(que guarda los parametros del usuario a registrar) a la listaUsuarios
    listaUsuarios.append(usuario)
else:
    #imprimimos html con ese mensaje
    #le pasamos el mensaje al html donde pone texto
    codigoHtml.error("Usuario repetido")
    # sale del python(de la ejecucion)
    exit()

#funcion que escribe los usuarios registrados en el fichero
#abrir, escribir y cerrar fichero
with open(fichUsu, "wt") as fichero:
    #lo convierte a json
    json.dump(listaUsuarios, fichero)

codigoHtml.correcto()
