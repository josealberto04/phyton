#Crear una función que calcule la temperatura media de un día a partir de la temperatura máxima y mínima. Crear un programa principal, que utilizando la función anterior, vaya pidiendo la temperatura máxima y mínima de cada día y vaya mostrando la media. El programa pedirá el número de días que se van a introducir.

def temperaturaMedia(tempmax,tempmin):
    media=(tempmax+tempmin)/2
    return media







dias= (int)(input("¿Cuántos días desea estudiar?: "))
for i in range (dias):
    tempmax=(int)(input("Introduzca la temperatura máxima: "))
    tempmin=(int)(input("Introduzca la temperatura mínima: "))
    print(temperaturaMedia(tempmax,tempmin))
    

