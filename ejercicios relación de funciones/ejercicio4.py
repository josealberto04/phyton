#Crea un función “ConvertirEspaciado”, que reciba como parámetro un texto y devuelve una cadena con un espacio adicional tras cada letra. Por ejemplo, “Hola, tú” devolverá “H o l a , t ú “. Crea un programa principal donde se use dicha función.

def convertirEspacio(texto):
    cadena= ""
    for i in texto:
        cadena=cadena+i+ " "

    return cadena


texto= input("Introduzca un texto: ")
print (convertirEspacio(texto))



