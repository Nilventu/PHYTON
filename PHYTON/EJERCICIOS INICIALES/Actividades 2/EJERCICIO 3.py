#21. Programa que calcula una ecuación de segundo grado. Controla que el valor de la raíz cuadrada no de un valor negativo
import math
a=float(input("Introduce el valor a: "))
b=float(input("Introduce el valor b: "))
c=float(input("Introduce el valor c: "))

op1=b**2-4*a*c
raiz=math.sqrt(op1)
if raiz<0:
    print("La raíz no puede ser un valor negativo")
op.resta=(-b-raiz)/2*a
op.suma=(-b+raiz)/2*a
print("El valor de x1 es:", op.resta)
print("El valor de x2 es:", op.suma)
