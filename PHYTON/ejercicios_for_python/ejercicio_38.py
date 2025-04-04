# 38. A partir del programa anterior, establece los rangos para que el usuario no pueda introducir notas inferiores a 0 y superiores a 10
nota=0
num_notas = int(input("Introduce el número de notas: "))
for i in range(num_notas):
    nota = float(input(f"Introduce la nota {i+1}: "))
    if nota>=0 and nota<=10:
        if nota >= 5:
            print("Asignatura aprobada")
        else:
            print("Asignatura suspendida")
        
    else:
        print("Has introducido una nota equivocada.")
