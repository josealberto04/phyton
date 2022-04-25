#Realizar un programa que comprueba si una cadena leída por teclado comienza por una subcadena introducida por teclado.

cadena= input("Dime una cadena: ")
subcadena= input("Dime una subcadena: ")
if (subcadena==cadena[0:len(subcadena)]):
    print("La cadena leía por teclado SÍ comienza por la subcadena introducida por teclado")
else:
    print("La cadena leía por teclado NO comienza por la subcadena introducida por teclado")