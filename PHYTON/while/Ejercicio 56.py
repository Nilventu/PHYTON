#57. Realiza un programa que permita adivinar un número comprendido entre 1 y 5. El programa debe controlar si el usuario introduce un número no comprendido entre 1 y 5
import random
x=0
radom=int(random.randint(1,5))
while x != radom:
    x= int(input("inserta un nimero entre 1-5: "))
    if x != radom:
        print("Número no acertado")
print("Número acertado")

