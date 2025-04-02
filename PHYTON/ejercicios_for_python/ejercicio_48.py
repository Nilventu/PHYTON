# Comprobar letras en la palabra secreta
palabra_secreta = input("Introduce la palabra secreta: ")
for i in range(len(palabra_secreta)):
    letra = input("Introduce una letra: ")
    if letra in palabra_secreta:
        print("La letra existe")
    else:
        print("La letra no existe")