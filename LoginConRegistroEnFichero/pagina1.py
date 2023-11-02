#!C:\Users\zx22student3208\AppData\Local\Programs\Python\Python311\python.exe

import codigoHtml
import http.cookies, os

if os.environ.get("HTTP_COOKIE") == None:
    codigoHtml.error("No estas logeado en el sistema")
    exit()
    
cookie = http.cookies.SimpleCookie()
cookie.load(os.environ.get("HTTP_COOKIE"))

if "Usuario" in cookie:
    codigoHtml.application("pagina 1","pagina2.py")
else:
    codigoHtml.error("No estas logeado en el sistema")

