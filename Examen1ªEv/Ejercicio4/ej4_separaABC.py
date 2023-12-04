#!C:\Users\zx22student3208\AppData\Local\Programs\Python\Python311\python.exe

#trabajar con cookies: Il tratar la informacion que va en la cookie
# los casos son! # el cliente NO me envia cookies -> crear cookie
# el cliente me envia cookies pero no esta la que busco -> crear cookie # el cliente me envia cookies Y esta la que busco -> Teer cookie y modificar
import http.cookies, os
from urllib.parse import urlparse, parse_qs
ru = os. environ. get("REQUEST_URI")
parametros = urlparse(ru)
param = parse_qs(parametros[4])

texto = param["texto"][0]

if texto.startswith("ABC"): 
    print("Content-Type: text/html") 
    cookie = http.cookies.SimpleCookie()

    if os.environ.get("HTTP_COOKIE") == None: 
        cookie["empiezaABC"] = 1 
        cookie["empiezaABC"] ["expires"] = "Wed, 11 Oct 2024 07: 28:00 GMT" 
        print (cookie["empiezaABC"])
        print()
    else:
        cookie. load(os. environ.get("HTTP_COOKIE") ) 
        if "empiezaABC" not in cookie: 
            cookie["empiezaABC"] = texto 
            cookie["empiezaABC"]["expires"] = "Wed, 11 Oct 2024 07:28:00 GMT" 
            print(cookie)
            print()
        else:
            cookie["empiezaABC"] = cookie["empiezaABC"] + " " + texto 
            cookie["empiezaABC"]["expires"] = "Wed, 11 Oct 2024 07: 28:00 GMT" 
            print(cookie)
            print()
