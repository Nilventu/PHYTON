#53. A partir del código anterior, haz que aparezca al finalizar el programa por pantalla el total las sumas y el número de repeticiones. Con While
sn=""
suma=0
repes=0
while sn!="n":
    var1= int(input("Introduce un valor: "))
    var2= int(input("Introduce otro valor: "))
    resultado = var1+var2

    repes=repes+1
    suma= suma + resultado
    print(f"El resultado de la suma es:{resultado}")
    
    sn=input("Deseas repetir la operación s/n: ")
    print(" ")
print(" ")
print("Mensaje resumen")
print(f"la suma total es: {suma} y el número de repeticiones es: {repes}")


    