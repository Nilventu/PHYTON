#54. Modifica el programa anterior y haz que se repita el ciclo automáticamente hasta que el total de todas las sumas sea superior a 50, será entonces cuando el programa finalice. No hará falta preguntar si deseas repetir la operación. En cada operación aparece por pantalla la suma de la operación y su acumulado. Para aquellos de vosotros que os fijáis en los detalles, controlar que el mensaje del acumulado es singular o plural.. . Con While
resultado=0
suma=0
repes=0
while suma <50:
    var1= int(input("Introduce un valor: "))
    var2= int(input("Introduce otro valor: "))
    resultado = var1+var2

    repes=repes+1
    suma= suma + resultado
    print(f"El resultado de la suma es:{suma}")
    print(f"El total acumulado es:{suma} y llevas {repes} operación realizada")
    print("")

print("“Fin del programa”")


    