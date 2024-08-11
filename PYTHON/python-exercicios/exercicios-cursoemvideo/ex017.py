#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo. Calcule e mostre o comprimento da hipotenusa
catop = float(input("Digite o cateto oposto: "))
catad = float(input("Digite o cateto adjacente: "))
hip = (catop ** 2 + catad ** 2) **(1/2)
print(f"A hipotenusa vai medir: {hip}")