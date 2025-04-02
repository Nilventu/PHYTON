# Programa que repite tu nombre un número de veces introducido por el usuario
nombre = "Alejandro De La Torre"
veces = int(input("Introduce el número de veces que quieres ver tu nombre: "))
for _ in range(veces):
    print(nombre)