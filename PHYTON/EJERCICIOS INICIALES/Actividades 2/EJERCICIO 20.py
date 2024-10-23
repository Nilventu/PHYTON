#20. A partir del ejercicio anterior, forzar que el usuario solo pueda introducir por teclados números entre 0 y 10
var1=int(input("Introduce el primer valor: "))
var2=int(input("Introduce el segundo valor: "))
if var1>10 or var1<0 and var2>10 or var2<0:
    print("Uno o los dos números están fuera de los límites establecidos"):
elif var1<var2:
    print("El número",var2," es mayor que el número",var1)
elif var1>var2:
    print("El número",var1," es mayor que el número",var2)
elif var1==var2:
    print("Ambos números son iguales",)
else:
    print("ERROR")