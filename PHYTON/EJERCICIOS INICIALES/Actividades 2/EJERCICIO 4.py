#22. Programa que al introducir una nota por teclado te diga si has aprobado o suspendido. Si la nota es menos de un 5 es suspenso y si la nota es 5 o mayor estás aprobado.

nota=float(input("Inserta tu nota"))
round(nota, 1)
if nota>=5:
    print("Has sacado un", nota," y has aprobado")
if nota<5:
    print("Has sacado un", nota," y has suspendido")
else:
    print("ERROR")
    