#Si tenemos una cadena con un nombre y apellidos, realizar un programa que muestre las iniciales en mayúsculas.

#(lower-para pasar todo a minúscula)

cadena=input("Introduce tu nombre y apellidos: ").lower()
print(cadena[0].upper(), end="")
contador=1

while(contador<len(cadena)):
    if (cadena[contador]==" "):
        print(" ",cadena[contador+1].upper(), end="")
        contador=contador+1
    else:
        print(cadena[contador], end="")
    contador=contador+1
