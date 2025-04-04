#46. A partir del programa anterior, soluciona el error que se produce en el test anterior con la palabra Abrigo utilizando únicamente una instrucción.
palabra = input("Introduce una palabra: ")
vocales = "aeiouAEIOU"

vocales_lista = ""
consonantes_lista = ""

for letra in palabra.lower():
    if letra in vocales:
        vocales_lista += letra
    else:
        consonantes_lista += letra
        
print(f"Las vocales de la palabra {palabra} son: {vocales_lista}")
print(f"Las consonantes de la palabra {palabra} son: {consonantes_lista}")
