#16. Utiliza el método sqrt de la librería math para calcular la raíz cuadrada de un número. Elresultado de la raíz cuadrada divídelo entre 2 de manera que se obtenga siempre unresultado entero. Haz que se muestre por pantalla los dos resultados de todo el proceso(raíz y división).
import math
valor=float(input("Escribe un valor:"))
raiz= math.sqrt(valor)
division=raiz/2
division=int(division)
print("El resultado de la raíz es: ", raiz)
print("El resultado de la división es: ",division)
      
