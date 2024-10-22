#21. Programa que calcula una ecuación de segundo grado. Controla que el valor de la raíz cuadrada no de un valor negativo
import math
a=int(input("Introduce el valor a: "))
b=int(input("Introduce el valor b: "))
c=int(input("Introduce el valor c: "))

raiz=math.sqrt((b**2)-(4*a*c))
if raiz < 0:
    print("La raíz no puede ser un valor negativo")

print("El valor de x1 es:", (-b + raiz)/(2*a))
print("El valor de x2 es:", (-b - raiz)/(2*a))