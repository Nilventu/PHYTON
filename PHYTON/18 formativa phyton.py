#18. Cines Paradiso celebran su décimo aniversario y por ser un día especial realizanimportantes descuentos. A los adultos se les aplicará un 10% de descuento y a los menoresde 18 años un 50%. Si la entrada cuesta 12 euros, calcula el total a pagar introduciendo porteclado el número de menores y el número de adultos que asisten al cine.
Menores=int(input("número de menores: "))
Adultos=int(input("número de adultos: "))

Precio_Adultos=Adultos*12
Porcentaje_Adultos=Precio_Adultos*0.10
Total_Adultos=Precio_Adultos-Porcentaje_Adultos

Precio_Menores=Menores*12
Porcentaje_Menores=Precio_Menores*0.50
Total_Menores=Precio_Menores-Porcentaje_Menores

print("El precio total del cine para",Menores," menor/es es: ",Total_Menores)
print("El precio total del cine para",Adultos," Adulto/s es: ",Total_Adultos)
