#40. Crea un programa que cuente todos los números pares hasta el número 50
pares = 0
impares = 0
for i in range(1, 51):
    if i % 2 == 0:
        pares += 1
    if i % 2 == 1:
        impares += 1
print(f"Total pares: {pares}")
print(f"Total impares: {impares}")
