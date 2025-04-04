# 48. Realiza un programa que introduzcas por teclado una palabra ‘secreta’, consigue la longitud deesa palabra para que sea ese el criterio que establezca el rango del bucle de manera que el usuariotenga x oportunidades para ver si letra introducida está en esa palabra.

palabra = input("Introduce la palabra : ")
for i in range(len(palabra)):
    letra = input("Introduce una letra: ")
    if letra in palabra:
        print("La letra existe")

    else:
        print("La letra no existe")
