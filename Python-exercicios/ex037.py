#Escreva um programa que leia um numero inteiro qualquer e peça para o usuario escolher qual será a base de conversão:
#1 binario
#2 octal
#3 hexadecimal
n = int(input("Digite um numero qualquer: "))
print(f'''Escolha uma das opções abaixo: 
[1] Converter {n} para Binário.
[2] Converter {n} para Octal. 
[3] Converter {n} para Hexadecimal.''')
opção = int(input("Digite uma opção: "))
if opção == 1:
    print(f"O numero {n} em Binario é: {bin(n)[2:]}")
elif opção == 2:
    print(f"O numero {n} em Octal é: {oct(n)}")
elif opção == 3:
    print(f"O numero {n} em hexadecimal é: {hex(n)}")
else:
    print("Opção invalida")