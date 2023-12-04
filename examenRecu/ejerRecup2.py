#!C:\Users\zx22student3208\AppData\Local\Programs\Python\Python311\python.exe

#Ejercicio 2, funcion para aplicar descuentos dependiendo del cliente y la ubicacion

print("Content-type: text/html\n")

# funcion para calcular el precio, a la que le pasamos los 3 valores
def calcular_precio_final(percio_base, tipo_cliente, ubicacion):
    precio_final = percio_base;
    # si el tipo de cliente es estudiante le rebajamos un 10% por lo que multiplicamos el valor por 0.9
    if (str(tipo_cliente)).lower() == "estudiante":
        precio_final = percio_base*0.9
        # Si el cliente esta fuera se le aplica un extra de recargo del 0.05 o del 5%
        if (str(ubicacion)).lower() == "fuera":
            precio_final += percio_base*0.05
    # si el tipo de cliente es miembro le rebajamos un 15% por lo que multiplicamos el valor por 0.85
    elif (str(tipo_cliente)).lower() == "miembro":
        precio_final = percio_base*0.85
        # Si el cliente esta fuera se le aplica un extra de recargo del 0.05 o del 5%
        if (str(ubicacion)).lower() == "fuera":
            precio_final += percio_base*0.05
    return precio_final

print(calcular_precio_final(100,"estudiante", "fuera"))
print(calcular_precio_final(50,"estudiante", "casa"))
print(calcular_precio_final(100,"miembro", "fuera"))
print(calcular_precio_final(100,"miembro", "casa"))
