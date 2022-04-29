#Realizar un programa que lea una cadena por teclado y convierta las  mayúsculas a minúsculas y viceversa

cadena= input("Introduce una cadena: ")
tamaño=len(cadena) -1
i=0

while i<= tamaño:
    if cadena[i]== cadena [i].upper():
        print(cadena[i].lower(), end="")
    else:
        print(cadena[i].upper(), end="")
    i=i+1