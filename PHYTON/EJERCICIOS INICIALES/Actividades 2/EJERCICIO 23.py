#23. Modifica el programa anterior para establecer si la nota es un excelente (8.5 a 10), un notable (>=6.5 -<8.5), satisfactorio (<6.5 -5) o insuficiente (<5). Controla que la nota introducida esté entre 0 y 10. Utilizar elif sin operadores lógicos.
nota=float(input("Inserta tu nota: "))
round(nota, 1)
if nota>=0 and nota <5:
    print("Has sacado un", nota," has sacado un insuficiente")
elif nota>=5 and nota <=6:
    print("Has sacado un", nota," has sacado un satisfactorio")
elif nota>6 and nota <=8.5:
    print("Has sacado un", nota," has sacado un notable")
elif nota>8.5 and nota <=10:
    print("Has sacado un", nota," has sacado un excelente")

else:
    print("ERROR")
    
