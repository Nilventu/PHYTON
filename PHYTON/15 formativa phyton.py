#15. Utiliza el valor Pi de la librería math para calcular el área y volumen de un cilindro,introduciendo por teclado el valor de radio y altura. Resultado con 2 decimales.
import math
radio=float(input("¿cuanto mide el radio?: "))
altura=float(input("¿cuanto mide la altura?: "))
volumen=math.pi*radio**2*altura
area=2*math.pi*radio*altura+2*math.pi*radio**2
print("El área de un cilindro es: ",round(area,2))
print("El volumen de un cilindro es: ",round(volumen,2))

