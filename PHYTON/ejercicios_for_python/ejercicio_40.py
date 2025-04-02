# Programa que cuenta todos los números pares hasta 50
pares = 0
for i in range(1, 51):
    if i % 2 == 0:
        pares += 1
print(f"El total de números pares hasta 50 es: {pares}")