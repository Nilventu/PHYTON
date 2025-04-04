#49. A partir del programa anterior, modifica el código para que al introducir la letra por teclado teindique en qué posición de la palabra se encuentra la letra.

palabra = input("Introduce la palabra secreta: ")
for i in range(len(palabra_secreta)):

    letra = input("Introduce una letra: ")
    if letra == palabra[i]:
        print(f"La letra se encuentra en la posición {i + 1}")
