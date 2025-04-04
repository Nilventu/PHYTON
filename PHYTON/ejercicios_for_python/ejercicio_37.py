#37. Programa que pregunte cuantas notas quiero introducir y para cada nota diga si estoy aprobado o suspendido.
num_notas = int(input("Introduce el número de notas: "))
for i in range(num_notas):
    nota = float(input(f"Introduce la nota {i+1}: "))
    if nota >= 5:
        print("Asignatura aprobada")
    else:
        print("Asignatura suspendida")
