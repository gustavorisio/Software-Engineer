#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. 
#No final, mostre os 10 primeiros termos dessa progressão.
print("============================")
print("    10 TERMOS DE UMA PA")
print("============================")
n = int(input("Primeiro termo: "))
razao = int(input("Digite a razão: "))
decimo = n + (10-1) * razao
for c in range(n,decimo+razao,razao):
    print(c, end = ' > ')
print("Acabou.")