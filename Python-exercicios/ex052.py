#Faça um programa que leia um numero inteiro e diga se ele é ou não um numero primo.
n = int(input("Digite um numero inteiro: "))
cont = 0
for c in range(1, n+1):
    if n % c == 0:
        print(f" Primo:[{c}]", end=" ")
        cont = cont + 1
    else:
        print(f" {c}", end=" ")
print(f"O numero {n} foi divisivel por ele mesmo {cont} vezes")