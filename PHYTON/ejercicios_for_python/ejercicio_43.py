# Recorrer una palabra y mostrar cada letra con su posición
palabra = input("Introduce una palabra: ")
for i in range(len(palabra)):
    print(f"En la posición {i} está la {palabra[i]}")