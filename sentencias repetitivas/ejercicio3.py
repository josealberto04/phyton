#Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir la suma y la media de todos los números introducidos.

vNum=[]
#contador=0
numero=(int)(input("Escriba un número: "))
if numero !=0:
    vNum.append(numero)
    #contador=contador+1
        

while numero!=0:
    numero=(int)(input("Escriba un número: "))
    if numero!=0:
        vNum.append(numero)
        #contador=contador+1
    
print("Has escrito ", len(vNum), " números y son: ", vNum)

#Suma de los números
suma=0
for i in vNum:
    suma=suma+i
    
print("La suma de estos números es ",suma)

#Media de los números
print("La media de estos números es ",suma/len(vNum))


