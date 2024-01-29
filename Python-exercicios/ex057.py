#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'
#Caso esteja errado, peça a d5igitação novamente até ter um valor correto.
sexo = str(input("Digite o sexo [M] Masculino ou [F] Feminino: ")).upper()
while sexo != 'M' and sexo != 'F':
    sexo = str(input("Sexo invalido. Tente novamente."))
print(f"Voce digitou o sexo {sexo}")
    
