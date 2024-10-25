#28. Mejora el programa anterior para controlar también la introducción de símbolos. Utiliza elif.
letra= input("Inserta letra o digito: ")

if letra.isupper():
    print("La letra es mayúscula")
elif letra.islower():
    print("La letra es mayúscula")
elif letra.isdigit():
    print("El digito es un número")

else:
    print("¿La letra es mayúscula?")