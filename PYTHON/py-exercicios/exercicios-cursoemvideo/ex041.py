#A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria de acordo com a idade:
#até 9 anos = Mirim
#até 14 anos = infantil
#até 19 anos = junior
#até 25 anos = senior
#acima de 25 anos = master
from datetime import date
atual = date.today().year
nascimento = int(input("Digite o ano do seu nascimento: "))
anos = atual - nascimento
if anos >=1 and anos <=9:
    print(f"Voce nasceu no ano de {nascimento}, a sua idade: {anos} anos.")
    print("Você está classificado como: Mirim.")
elif anos >=10 and anos <=14:
    print(f"Voce nasceu no ano de {nascimento}, e a sua idade atual: {anos} anos.")
    print("Você está classificado como: Infantil.")
elif anos >=15 and anos <=19:
    print(f"Voce nasceu no ano de {nascimento}, e a sua idade atual: {anos} anos.")
    print("A sua classificação é: JUNIOR.")
elif anos >=20 and anos <=25:
    print(f"Voce nasceu no ano de {nascimento}, e a sua idade atual: {anos} anos.")
    print ("Você está classificado como: Senior.")
elif anos >=26 and anos <=100:
    print(f"Voce nasceu no ano de {nascimento}, a sua idade atual: {anos} anos.")
    print("Você está classificado como MASTER.")
else:
    print("Não foi possível classificar com o ano de nascimento informado, tente novamente.")
