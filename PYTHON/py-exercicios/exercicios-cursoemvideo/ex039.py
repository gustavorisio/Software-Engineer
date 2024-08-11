#Faça um programa que leia o ano de nascimento do candidato jovem e informe de acordo com a sua idade, 
# Se ele ainda vai se alistar ao serviço militar, se é a hora de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from time import sleep
from datetime import date
nascimento = int(input("Digite o seu ano de nascimento: "))
ano = date.today().year
idade = ano - nascimento
print("Processando... Aguarde...")
sleep(2)
if idade > 30:
    passou = idade - 18
    print(f"Quem nasceu em {nascimento} tem {idade} anos em {ano}.")
    print(f"Você não pode se alistar, a idade minima para alistamento é dos 18 até os 30 anos. De acordo com a sua idade já se passaram {passou} anos.")
elif idade == 18:
    print(f"Quem nasceu em {nascimento} tem {idade} anos em {ano}.")
    print("Voce tem que se alistar imediatamente.")
elif idade < 18:
    falta = 18 - idade
    sera = ano + idade
    print(f"Quem nasceu em {nascimento} tem {idade} anos em {ano}.")
    print(f"Você não pode se alistar até completar 18 anos. Você poderá se alistar daqui {idade} anos, no ano de {sera}.")
    print("Procure um posto de atendimento na sua cidade.")
else:
    ate = ano + idade
    print(f"Quem nasceu em {nascimento} tem {idade} anos em {ano}.")
    print(f"Você pode se alistar até {ate}!")

