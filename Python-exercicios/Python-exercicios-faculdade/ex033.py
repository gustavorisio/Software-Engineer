#Criar um algoritmo que imprima na tela os números de 1 a 100 exceto os números múltiplos de 3
lista = []
for n in range(101):
    if n % 3 != 0:
        lista.append(n)
print(lista)