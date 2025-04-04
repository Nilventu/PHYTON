# 35.Programa que al introducir un número por teclado permita mostrar ese número de veces tu nombre
nombre = input("introduce un nombre: ")
veces = int(input("Introduce el número de veces que quieres ver tu nombre: "))
for _ in range(veces):
    print(nombre)
