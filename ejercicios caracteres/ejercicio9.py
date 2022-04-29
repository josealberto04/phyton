#Realizar un programa que compruebe si una cadena contiene una subcadena.  Las dos cadenas se introducen por teclado.

cadena=input("Introduce una cadena: " )
subcadena= input ("Introduce una subcadena: ")

if cadena.find(subcadena)!=-1:
    print("La subcadena está dentro de la cadena")
else:
    print("La subcadena no está dentro de la cadena")