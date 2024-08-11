#Criar um algoritmo (Fluxograma) que leia o saldo de uma aplicação e imprimir 
#o novo saldo, considerando um reajuste de 15%.
saldo = int(input("Digite o valor do saldo: "))
novosaldo = saldo + saldo * 15/100
print(f"o novo saldo é de R${novosaldo}")