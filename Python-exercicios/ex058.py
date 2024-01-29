#Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um numero entre 0 e 10. 
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessarios para vencer.
from random import randint
from time import sleep
n = randint (0, 10)
print("==================================================================================")
escreva = int(input("Qual numero o computador está sorteando? Digite um numero de 0 a 10: "))
print("==================================================================================")
print(f"O numero que voce digitou é: {escreva}")
print(f"Processando o resultado do sorteio...")
sleep(2)
while escreva != n: 
    print("============================")
    print(f"Você errou! Tente novamente! ")
    print("============================")
    escreva = int(input("Qual seu palpite? "))
    print(f"Processando o resultado do sorteio...")
    sleep(2)
    if escreva == n:
        print("=======================================")
        print("Parabéns voce ACERTOU!!")
        print(f"O numero que o computador sorteou é: {n}")
        print("=======================================")
