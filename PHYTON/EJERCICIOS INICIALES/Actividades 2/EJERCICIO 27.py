#27. Mejora el programa anterior para controlar que el valor #26. Realiza un programa que, al introducir una letra por teclado, aparezca por pantalla si está o no en mayúscula. Utiliza dos IF’s que establezcan True o False a la condición
letra= input("Inserta letra o digito: ")

if letra.isupper():
    print("La letra es mayúscula")
elif letra.islower():
    print("La letra es mayúscula")
elif letra.isdigit():
    print("El digito es un número")

else:
    print("¿La letra es mayúscula?")
    