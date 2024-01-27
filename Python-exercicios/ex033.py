#Faça um programa que leia tres numeros e descubra qual deles é o maior e o menor numero.
n1 = int(input("Digite um numero: "))
n2 = int(input("Digite um outro numero: "))
n3 = int(input("Digite mais um numero: "))
#verificando se n1 é menor
if n1 < n2 and n1<n3:
    print(f"O numero {n1} é menor.")
#verificando se n2 é menor
if n2 < n1 and n2 < n3:
    print(f"O numero {n2} é menor.")
#verificando se n3 é menor
if n3 < n1 and n3 < n2:
    print(f"O numero {n3} é menor.")
#verificando se n1 é maior
if n1 > n2 and n1 > n3:
    print(f"O numero {n1} é maior.")
#verificando se n2 é maior
if n2 > n1 and n2 > n3:
    print(f"O numero {n3} é maior.")
#verificando se n3 é maior
if n3 > n1 and n3 > n2:
    print(f"O numero {n3} é maior.")