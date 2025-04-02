# Programa que verifica si las notas están en el rango de 0 a 10
num_notas = int(input("Introduce el número de notas que deseas introducir: "))
for i in range(num_notas):
    while True:
        nota = float(input(f"Introduce la nota {i+1}: "))
        if 0 <= nota <= 10:
            if nota >= 5:
                print("Asignatura aprobada")
            else:
                print("Asignatura suspendida")
            break
        else:
            print("Has introducido una nota equivocada.")