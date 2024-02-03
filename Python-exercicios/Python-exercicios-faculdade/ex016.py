#Sabe-se que para iluminar de maneira correta os cômodos de uma casa, para cada 
#metro quadrado, deve-se usar 18W de potência. Faça um algoritmo
#que receba as duas dimensões de um cômodo (em metros). Calcule e mostre a sua 
#área (em m2) e a potência de iluminação que deverá ser utilizada
d1 = float(input("Digite o primeiro valor da dimensão do comodo em metros: "))
d2 = float(input("Digite o segundo valor da dimensão do comodo em metros: "))
area = d1 * d2
potencia = area * 18
print(f"Potencia em (Watts) para iluminar o comodo: {potencia}w")
print(f"A area calculada em m² é de {area}m²")