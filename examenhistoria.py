#Devolvemos el nombre con más probabilidad: Franco o Guerra Civil

import random

def francoVSguerraCivil(ite): #ite son las iteraciones que vamos a realizar
    contadorguerraCivil=0
    contadorfranco=0
    numAleatorio=0
    total=ite
    while(ite!=0):
        numAleatorio = random.randint(1,2)
        if numAleatorio==1:
            contadorguerraCivil=contadorguerraCivil+1
        else:
            contadorfranco=contadorfranco+1

        ite=ite-1
   
    print("La probabilidad de que salga la Guerra Civil es: ",((contadorguerraCivil/total)*100))
    print("La probabilidad de que salga Franco es: ",(contadorfranco/total)*100)


ite=(int)(input("¿Cuántas veces quieres comprobar?: "))
print(francoVSguerraCivil(ite))
 