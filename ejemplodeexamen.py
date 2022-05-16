#Ejemplo de examen    Crea una función que delvuelva una lista de número aleatorios y se van insertando cada medio segundo. 
import random
import time


def generarLista(numelem):
    num=0
    v=[]
    for i in range(0,numelem):
        num=random.randint(0,10)
        time.sleep(0.5)
        v.append(num)
    return v


bandera= True
while bandera== True:
    try:
        x= int (input("¿Cuántos números desea introducir?: "))
        print(generarLista(x))
        bandera=False
    except:
        print ("Por favor introduzca un número")
        bandera=True







