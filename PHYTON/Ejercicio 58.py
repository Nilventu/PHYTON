#58. Modifica el programa anterior para que tengas 3 intentos. Utiliza while
import random
repes=0
x=0
radom=int(random.randint(1,5))
while x != radom and repes<3:
    x= int(input("inserta un nimero entre 1-5: "))
    if x != radom:
        print("Número no acertado")
        repes+=1
    else:
        print("Número acertado")

