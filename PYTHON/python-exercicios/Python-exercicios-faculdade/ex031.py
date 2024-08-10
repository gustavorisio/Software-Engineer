#Criar um algoritmo que receba N números e imprima o quadrado de cada número
n = int(input("Quantos numeros voce deseja calcular o quadrado? "))

numeros = []
for i in range(n):
    num = float(input(f"Digite o numero {i+1} > "))
    numeros.append(num)
    
print("Os quadrados dos numeros digitados são: ")
if num in numeros:
    quad = num ** 2
    print(f"O resultado de {num} é {quad}")
