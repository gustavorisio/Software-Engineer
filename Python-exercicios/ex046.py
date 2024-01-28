#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio
#Indo de 10 até 0, com uma pausa de 1 segundo entre eles.
from time import sleep
contagem = 10
for c in range(contagem, -1, -1):
    print("...")
    sleep(1)
    print(f"{c} s")