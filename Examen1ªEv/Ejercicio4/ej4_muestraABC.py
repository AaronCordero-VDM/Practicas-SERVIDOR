#!C:\Users\zx22student3208\AppData\Local\Programs\Python\Python311\python.exe

import http.cookies, os import codigoHTML
cookie = http.cookies. SimpleCookie()
print("Content-type: text/html\n")
if os.environ.get("HTTP_COOKIE") != None: 
    cookie. load(os.environ.get("HTTP_COOKIE")) 
    if "empiezaABC" in cookie: 
    codigoHTML.cabHTMLGen()
    listaPalabras = cookie["empiezaABC"]. value.split(" ")
    print("<ol>") 
    for item in listaPalabras: 
        print(f"<li>{item}</li>") 
        print("</ol>") 
        codigoHTML. finHTMLGen()