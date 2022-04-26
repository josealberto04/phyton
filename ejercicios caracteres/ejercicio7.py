#Pide una cadena y dos caracteres por teclado (valida que sea un carácter), sustituye la aparición del primer carácter en la cadena por el segundo carácter.

cadena= input("Introduce una cadena: ")
caracter1= input("Introduce un carácter: ").upper()
caracter2= input("Introduce un carácter: ").upper()
cadena2= ""

caracter1=ord(caracter1)
caracter2=ord(caracter2)
if ((caracter1>=65 and caracter1<=90) and  (caracter2>=65 and caracter2<=90)):
    print("Los carácteres son válidos")
else:
     print("Por favor, introduzca otros carácteres")

i=0
tamaño=len(cadena)
while i<tamaño:
    if cadena[i]==chr(caracter1).lower():
        cadena2= cadena2 + chr(caracter2).lower()
    else:
        cadena2=cadena2+cadena[i]
    i=i+1
print(cadena2)