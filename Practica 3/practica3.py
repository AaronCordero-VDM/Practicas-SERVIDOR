#!C:\Users\zx22student3208\AppData\Local\Programs\Python\Python311\python.exe

print("Content-type: text/html\n")

print("Un cambio 2.0")


numero = 5
texto = "5"

print(numero) #Imprime el valor de la variable
print(type(numero)) #Imprime el tipo de variable 

print(texto)
print(type(texto))

x, y, z = "Orange", "Banana", "Cherry"  
#Asignar valor a varias variables a la vez. 
#El numero de variables a de ser igual al de asiganciones
#De lo contrario no asingnara ningun valor
print(x)
print(y)
print(z)

a = b = c = "Orange"  
#Asignara el mismo valor a todas las variables
print(a)
print(b)
print(c)

fruits = ["manzana","platano","pera"]
d,e,f = fruits
print(d)
print(e)
print(f)

numero=str(5)


#funciones
variable = "aaaaa"

def miFuncion():
    variable = "bbbbbbbbb"
    print(variable)
miFuncion()   
print(variable)
