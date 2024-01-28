#Crie um programa que faça o computador jogar Jokenpo com você.
from random import randint
itens = ("Pedra","Papel","Tesoura")
print("""JOKENPÔ!!!
Você irá enfrentar a IA, escolha uma opção:
[1] PEDRA
[2] PAPEL
[3] TESOURA""")
computador = randint(0,2)
opção = int(input("Digite uma opção: "))
if opção == 1: #Jogador escolheu PEDRA
    print("Você escolheu PEDRA.")
    print(f"O computador escolheu: {itens[computador]}")
    if computador == 0:
        print("EMPATE!")
    elif computador == 1:
        print("O computador VENCEU!")
    elif computador == 2:
        print("O jogador VENCEU!")
elif opção == 2: #Jogador escolheu PAPEL
    print("Você escolheu PAPEL.")
    print(f"O computador escolheu: {itens[computador]}")
    if computador == 0:
        print("O jogador venceu!")
    elif computador == 1:
        print("EMPATE!")
    elif computador == 2:
        print("O computador ganhou!")
elif opção == 3: #Jogador escolheu TESOURA
    print("Você escolheu TESOURA.")
    print(f"O computador escolheu: {itens[computador]}")
    if computador == 0:
        print("O computador VENCEU!")
    elif computador ==1:
        print("O jogador VENCEU!!")
    elif computador == 2:
        print("EMPATE!")
else:
    print("Erro. Tente novamente.")
    