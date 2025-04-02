# Programa que dice si una asignatura está aprobada o suspendida
num_notas = int(input("Introduce el número de notas que deseas introducir: "))
for i in range(num_notas):
    nota = float(input(f"Introduce la nota {i+1}: "))
    if nota >= 5:
        print("Asignatura aprobada")
    else:
        print("Asignatura suspendida")