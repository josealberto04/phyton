#Introducir una cadena de caracteres e indicar si es un palíndromo. Una palabra palíndroma es aquella que se lee igual adelante que atrás.
def inviertepalabra(cadena):
    i=len(cadena)
    subcadena=""
    while i>0:
        i=i-1
        subcadena= subcadena+cadena[i]
    return subcadena


cadena=input("Introduce una cadena: ")


if inviertepalabra(cadena)==cadena:
    print("La palabra introducida es un palíndromo")
else:
    print("La palabra NO es un palíndromo")