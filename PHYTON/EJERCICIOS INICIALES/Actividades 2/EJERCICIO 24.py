#25. Repite el programa número 23 pero en esta ocasión utilizando operadores lógicos.
nota=float(input("Inserta tu nota: "))
round(nota, 1)
if nota>=0 and nota <5:
    print("Has sacado un", nota," has sacado un insuficiente")
if nota>=5 and nota <=6:
    print("Has sacado un", nota," has sacado un satisfactorio")
if nota>6 and nota <=8.5:
    print("Has sacado un", nota," has sacado un notable")
if nota>8.5 and nota <=10:
    print("Has sacado un", nota," has sacado un excelente")

else:
    print("ERROR")
    