#26. Realiza un programa que, al introducir una letra por teclado, aparezca por pantalla si está o no en mayúscula. Utiliza dos IF’s que establezcan True o False a la condición
letra= input("Inserta la letra: ")

if letra.isupper():
    print("La letra es mayúscula")
elif letra.islower():
    print("La letra es mayúscula")
else:
    print("ERROR")
    