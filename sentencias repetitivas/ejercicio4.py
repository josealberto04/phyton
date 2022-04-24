#Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de números a introducir). El programa debe informar de cuantos números introducidos son mayores que 0, menores que 0 e iguales a 0.

igual=0
menor=0
mayor=0

cantidad= (int)(input("Introduce la cantidad de números que desee: "))

for i in range(0,cantidad):
    num= (int)(input("Introduce el número "))
    if num>0:
        mayor=mayor+1
    if num<0:
        menor=menor+1
    if num==0:
        igual=igual+1

print("Has introducido ",mayor," número mayores de 0, ", menor," números menores de 0 y ",igual ," números iguales de 0")

