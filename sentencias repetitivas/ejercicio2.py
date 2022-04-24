#Crea una aplicación que permita adivinar un número. La aplicación genera un número aleatorio del 1 al 100. A continuación va pidiendo números y va respondiendo si el número a adivinar es mayor o menor que el introducido,a demás de los intentos que te quedan (tienes 10 intentos para acertarlo). El programa termina cuando se acierta el número (además te dice en cuantos intentos lo has acertado), si se llega al limite de intentos te muestra el número que había generado.

import random

numAleatorio = random.randint(0,100)
intentos=10
numPedido=-1


numPedido= (int)(input("Dime un número: "))
while (intentos > 0):
    print("Este es el intento ", intentos )
    numPedido = (int)(input("Dime un número "))

    intentos=intentos-1
    if numPedido < numAleatorio:
        print("El número es mayor")

    if numPedido > numAleatorio:
            print("El número es menor")
    if numPedido==numAleatorio:
        break


if (intentos==0):
    print("Te han sobrado ", intentos, " intentos")
    print("El número que tenías que adivinar era ",numAleatorio)
else:
    print("Acertaste, te han sobrado ", intentos, " intentos")