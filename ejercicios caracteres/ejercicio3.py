#Pide una cadena y un carácter por teclado (valida que sea un carácter) y muestra cuantas veces aparece el carácter en la cadena.

cadena= input("Dime una cadena: ")
caracter= input("Dime un carácter: ").upper()
contador=0

caracter=ord(caracter)
if (caracter>=65 and caracter<=90):
    print("El carácter es válido")
    for aux in cadena:
        if (ord(aux.upper())==caracter):
            contador=contador+1
            

print("El carácter aparece " , contador, " veces")
