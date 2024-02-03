#Faça um algoritmo que receba um número positivo 
# e maior que zero, calcule e mostre:
# a) o número digitado ao quadrado;
# b) a raiz quadrada do número digitado;
n = int(input("Digite um numero positivo: "))
quadrado = n ** 2
raiz = n ** (1/2)
print(f"O numero {n} ao quadrado é: {quadrado}")
print(f"A raiz quadrada do numero {n} é: {raiz}")