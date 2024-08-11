#Criar um algoritmo (Fluxograma) que dados dois lados de um triângulo retângulo 
#calcule e exiba a respectiva hipotenusa
import math
lado1 = int(input("Digite o valor do primeiro triangulo: "))
lado2 = int(input("Digite o valor do segundo triangulo: "))
hipotenusa = math.sqrt(lado1 **2 + lado2 **2)
print(hipotenusa)