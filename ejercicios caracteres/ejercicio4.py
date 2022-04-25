#Suponiendo que hemos introducido una cadena por teclado que representa una frase (palabras separadas por espacios), realiza un programa que cuente cuantas palabras tiene.
contador=1
frase= input("Introduce una frase: ")
for i in frase:
    if i== " ":
        contador=contador+1

print("La frase tiene ", contador, " palabras")
