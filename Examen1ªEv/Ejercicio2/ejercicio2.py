#!C:\Users\zx22student3208\AppData\Local\Programs\Python\Python311\python.exe

#Ejercicio 2, recibir una lista y guardarla, al igual que una operacion, posteriromente 
# hacer el calculo oportuno

print("Content-type: text/html\n")

numeros = [100, 50, 65, 82, 23]
#funcion para hacer operaciones con numeros
def operacionesLista(numeros, operacion):
    #variable resultado que mostraremos al usuario
    resultado = 0
    #numeros es una lista de numeros(numeros=[1,30,42,45])
    #operacion es un caracter (operacion="")
    #La lista de numeros tiene que tener una longitud mayor que cero si no devolveremos un 0
    if len(numeros) > 0:
        #Si la operacion es suma
        if operacion == "+":
            #Sumaremos todos los numeros alamacenandolos en resultado
            for num in numeros: #Bucle que recorre la lista
                resultado += num
        #Si la operacion es multiplicar
        elif operacion == "*":
            #Resultado tiene que valer uno para que no multiplique por 0
            resultado = 1
            #Multiplicamos todos los numeros recorriendo la lista numeros
            for num in numeros:
                resultado *= num
        #Si la operacion no es ni suma ni multiplicacion resultado es -1
        else:
            resultado = -1
    #Si la lista esta vacia, resultado valdra 0
    else:
        resultado = 0
    #Devolvemos el resultado
    return resultado

operacionesLista()