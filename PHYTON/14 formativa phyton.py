#14. Realiza un programa que a partir de introducir el diámetro de un círculo calcule el área y perímetro. Importa la librería match y utiliza el valor PI para hacer el cálculo. Redondea el resultado a un decimal
Diametro=float(input("Introduce el diametro del circulo: "))
import math
radio=Diametro/2
area=radio**2*math.pi
print("La area es: ", area)

