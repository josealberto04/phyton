#Crea una función “calcularMaxMin” que recibe una arreglo con valores numérico  y devuelve el valor máximo y el mínimo. Crea un programa que pida números  por teclado y muestre el máximo y el mínimo, utilizando la función anterior.

def calcularMaxMin(vector):
    min = max = vector[0]
    vminmax=[]
    for i in vector:
        if min>i:
            min=i
        
        if max<i:
            max=i
    vminmax.append(min)
    vminmax.append(max)
    return vminmax
    


v=[]
cantidad= int(input("¿Cuántos números desea introducir?: "))
for i in range (cantidad):
    num= int(input("Introduce el número que desee: "))
    v.append(num)

resul=calcularMaxMin(v)

print("El mínimo es ",resul[0])
print("El máximo es ",resul[1])
