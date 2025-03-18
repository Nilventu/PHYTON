#61. A partir del código anterior, haz que el programa finalice si el valor de la tabla de multiplicar essuperior o igual a 40.
repes=1
var1=2
numero= int(input("introduce un numero: "))
while repes<11:
    resultado=var1*repes
    repes+=1
    print(f"{resultado}")
    if resultado>40:
        repes=50
        