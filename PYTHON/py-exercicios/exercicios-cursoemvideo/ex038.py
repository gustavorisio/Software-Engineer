#Escreva um programa que leia dois numeros inteiros e compara-os, 
# mostrando na tela uma mensagem: 
# - O primeiro valor é maior 
# - O segundo valor é menor 
# - Não existe valor maior, os dois são iguais
n1 = int(input("Digite um numero inteiro: "))
n2 = int(input("Digite outro numero inteiro: "))
if n1>n2:
    print(f"O primeiro numero {n1} é maior")
elif n2>n1:
    print(f"O segundo numero {n2} é maior")
if n1<n2:
    print(f"O primeiro numero {n1} é menor")
elif n2<n1:
    print(f"O segundo numero {n2} é menor")
else:
    print(f"Os dois numeros são iguais.")