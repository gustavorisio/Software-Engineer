n = int(input("Quantos números você deseja inserir? "))
numeros = []

for i in range(n):
    num = int(input(f"Digite o número {i+1}: "))
    numeros.append(num)

contador = 0
for num in numeros:
    if num % 2 == 0:
        contador += 1

print(f"\nDos {n} números digitados, {contador} são pares.")