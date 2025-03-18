#55. Última vez que reutilizamos el mismo código.. lo prometo . A partir del programa anterior haz que sea todo exactamente igual pero teniendo en cuenta que el programa se repita siempre y cuando la suma acumulada sea superior a 50 o la suma acumulada sea par. Con While
parimpar=""
resultado=0
suma=0
repes=0
while suma<50:
    var1= int(input("Introduce un valor: "))
    var2= int(input("Introduce otro valor: "))
    resultado = var1+var2
    repes=repes+1
    suma= suma+resultado
    print(f"El resultado de la suma es: {suma}")
    print(f"El total acumulado es:{suma} y llevas {repes} operación realizada")
    print("")
    
    if suma%2==0:
        break
print("“Fin del programa”")