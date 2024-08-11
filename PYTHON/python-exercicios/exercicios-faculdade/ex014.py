#Faça um algoritmo que receba o peso de uma pessoa em quilos. 
#Calcule e mostre: 
# a. O novo peso se a pessoa engordar 15% sobre o peso digitado;
# b. O novo peso se a pessoa emagrecer 20% sobre o peso digitado
peso = int(input("Digite o peso da pessoa em quilos: "))
engordar = peso + peso * 15/100
emagrecer = peso - peso * 20/100
print(f"A pessoa emagreceu, o seu novo peso é: {emagrecer} quilos. ")
print(f"A pessoa engordou, o seu novo peso é: {engordar} quilos. ")