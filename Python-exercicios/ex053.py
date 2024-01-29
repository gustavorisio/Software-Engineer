#Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços.
# EX: asacadadacasa, EX: Apos a sopa
frase = str(input("Digite uma frase: ")).upper()
separa = frase.split()
junto = "".join(separa)
print(f"A frase digitada é: {junto}")

