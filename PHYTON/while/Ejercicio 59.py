#59. Diseña un programa que “piense” un numero aleatorio entre 0 y 1000 para que nos pida que 
#intentemos adivinarlo. En cada intento, el programa nos dirá si el numero introducido es mayor o 
#menor del correcto. No utilices break para salir del bucle. Cuando se acierte el número debe 
#mostrarse por pantalla un mensaje y el número de intentos.

import random
respuesta=0
radom=int(random.randint(0,1000))

while respuesta != radom:
    respuesta=int(input("Introduce un valor comprendido entre 1 y 1000: "))
    
    if respuesta>radom:
        print("El número que has introducido es mayor")
 
    if respuesta < radom:
        print("El número que has introducido es menor")

print("Has acertado!")

        

    