#12. Realiza un programa que, introduciendo en los valores de lado, base menor, base mayor y altura de un trapecio isósceles, nos devuelva por pantalla en el área y el perímetro.
var1=int(input("Introduce  valor de lado: "))
var2=int(input("Introduce  valor de base mayor: "))
var3=int(input("Introduce  valor de basem menor: "))
var4=int(input("Introduce  valor de altura: "))
base_mayor=var2+var3
bases_2=base_mayor/2
area=bases_2*var4
print("El area es: ", area)
print("El  es perimetro es: ", var1*2 + var2 + var3)
