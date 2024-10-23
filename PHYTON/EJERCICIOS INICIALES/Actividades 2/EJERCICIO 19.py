#19. Programa que introduzca dos números y devuelva cuál de los dos es mayor, menor o son iguales
var1=int(input("Introduce el primer valor: "))
var2=int(input("Introduce el segundo valor: "))
if var1<var2:
    print("El número",var2," es mayor que el número",var1)
elif var1>var2:
    print("El número",var1," es mayor que el número",var2)
elif var1==var2:
    print("Ambos números son iguales",)
else:
    print("ERROR")
    
    