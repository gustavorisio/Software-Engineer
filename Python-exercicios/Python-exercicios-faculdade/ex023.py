#Construa um algoritmo que leia 3 valores inteiros e positivos e: encontre o maior 
#valor; encontre o menor valor e calcule a média dos números lidos.
n1 = int(input("Digite um valor: "))
n2 = int(input("Digite outro valor: "))
n3 = int(input("Digite o ultimo valor: "))
if n1 > n2 and n1 > n3:
    print(f"{n1} é o maior valor. ")
elif n2 > n1 and n2 > n3:
    print(f"{n2} é o maior valor. ")
elif n3 > n1 and n3 > n2:
    print(f"{n3} é o maior valor. ")
if n1 < n2 and n1 < n2:
    print(f"{n1} é o menor valor.")
elif n2 < n1 and n2 < n3:
    print(f"{n2} é o menor valor")
elif n3 < n1 and n3 < n2:
    print(f"{n3} é o menor valor.")
