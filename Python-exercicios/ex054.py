#Crie um programa que leia o ano de nascimento de sete pessoas. 
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
maioridade = 0
naomaior = 0
for p in range(1,5):
    nascimento = int(input(f"Em que ano a {p}º pessoa nasceu? "))
    idade = date.today().year - nascimento
    menor = date.today().year - 100
    print(f"{p}º Nasceu no ano: {nascimento}, a idade é de {idade} anos")
    if idade <=18:
        naomaior = naomaior + 1
    else:
        maioridade = maioridade + 1
print(f"{naomaior} pessoas não atingiram a maioridade")
print(f"{maioridade} pessoas são de maior.")