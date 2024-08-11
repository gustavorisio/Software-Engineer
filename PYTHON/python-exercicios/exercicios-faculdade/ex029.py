#Criar um codigo, utilizando a estrutura escolha, que mostre o menu de opções a 
#seguir, receba a opção do usuário e os dados necessários para executar cada operação.
#Menu de opções:
#1- Somar dois números.
#2- Multiplicar dois números
#3- Subtrair dois números
#4- Dividir dois números
n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))
print("""Opções:
[1] Soma
[2] Multiplicação
[3] Subtração
[4] Dividir dois numeros""")
opção = int(input("Escolha uma opção: "))
if opção == 1:
    soma = n1 + n2
    print(f"A soma dos dois valores é: {soma}")
if opção == 2:
    multi = n1 * n2
    print(f"Multiplicação dos dois numeros é: {multi}")
if opção == 3:
    subtração = n1 - n2
    print(f"A subtração dos dois numeros é: {subtração}")
if opção == 4:
    divisão = n1 / n2
    print(f"A divisão dos dois numeros é: {divisão}")
    