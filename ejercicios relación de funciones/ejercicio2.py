#Crea un programa que pida dos número enteros al usuario y diga si alguno de ellos es múltiplo del otro. Crea una función EsMultiplo que reciba los dos números, y devuelve si el primero es múltiplo del segundo.

def esMultiplo(n1,n2):
    resto=n1%n2

    if resto==0:
        return True
    else:
        return False

n1=(int)(input("Introduce un número: "))
n2=(int)(input("Introduce un número: "))

if(esMultiplo(n1,n2)==True):
    print("Es múltiplo")
else:
    print("No es múltiplo")


