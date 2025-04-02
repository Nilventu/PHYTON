# Indicar en qué posición de la palabra está la letra introducida
palabra_secreta = input("Introduce la palabra secreta: ")
for i in range(len(palabra_secreta)):
    letra = input("Introduce una letra: ")
    if letra == palabra_secreta[i]:
        print(f"La letra se encuentra en la posición {i + 1}")