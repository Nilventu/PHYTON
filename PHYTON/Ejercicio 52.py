#52. Realiza un programa que sume dos números enteros por teclado y presente el resultado por pantalla. El programa preguntará si deseas o no repetir la operación. Con While
sn=""
while sn!="no":
    var1= int(input("Introduce un valor: "))
    var2= int(input("Introduce otro valor: "))
    resultado = var1+var2

    print(f"El resultado de la suma es:{resultado}")
    
    sn=input("Deseas repetir la operación s/n: ")