#27. Mejora el programa anterior para controlar que el valor introducido es una letra y en caso de introducir un número, aparezca un aviso por pantalla
letra= input("Inserta letra o digito: ")

if letra.isupper():
    print("La letra es mayúscula")
elif letra.islower():
    print("La letra es minúcula")
elif letra.isdigit():
    print("El digito es un número")

else:
    print("¿La letra es mayúscula?") 
