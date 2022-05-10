#Crea un procedimiento EscribirCentrado, que reciba como parámetro un texto y lo escriba centrado en pantalla.
  
def escribirCentrado(texto):
    posicion=int(85-(len(texto)/2))
    textoCentrado= ""
    for i in range (0, posicion):
        textoCentrado=textoCentrado + " "   
    print(textoCentrado+texto)

texto= input("Introduzca un texto: ")
escribirCentrado(texto)