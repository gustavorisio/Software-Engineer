#Faça um algoritmo que leia a largura e a altura de uma parede em metros. 
#Calcule a sua area e a quantidade de tinta necessaria para pinta-la, sabendo que cada litro de tinta, pinta uma área de 2m². 
largura = float(input("Digite a largura da parede: "))
altura = float(input("Digite a altura da parede: "))
area = largura * altura
tinta = area / 2
print(f"A largura da parede é: {largura} e a altura é: {altura}. A quantidade de tinta necessaria para a area de {area}m² é de {tinta} litros")