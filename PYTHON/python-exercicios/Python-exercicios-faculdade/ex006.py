#Faça um algoritmo (Fluxograma e Pseudocódigo) que receba o ano de nascimento 
#de uma pessoa e o ano atual, calcule e mostre:
# a) A idade dessa pessoa;
# b) Quantos anos essa pessoa terá em 2030;
from datetime import date
ano = date.today().year
nascimento = int(input("Digite o seu ano de nascimento: "))
idade = ano - nascimento
ano2030 = 2030 - nascimento
print(f"O usuario tem {idade} anos no ano de {ano}")
print(f"No ano de 2030 o usuario terá: {ano2030} anos")

