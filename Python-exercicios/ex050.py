#Desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas daqueles que forem pares.
#Se o valor digitado for impar, desconsidere-o.
pares = 0
cont = 0
for c in range(1,7):
    numero = int(input(f"Digite o {c}º valor: "))
    if numero % 2 == 0:
        pares = numero + pares
        cont = cont + 1
print(f"Os numeros pares são: {cont} e a soma: {pares}")