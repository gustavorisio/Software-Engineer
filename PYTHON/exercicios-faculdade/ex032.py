#Criar um algoritmo lista que receba 20 números e imprima a metade de cada número
lista = []
for n in range(20):
    numero = int(input(f"Digite o {n+1}º numero: "))
    metade = numero / 2
    lista.append(metade)
    print(f"A metade desse numero é: {metade}")
print(lista)