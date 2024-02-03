#Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um 
#algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7 (h = altura
altura = float(input("Digite a altura da pessoa: "))
sexo = str(input("Digite o sexo da pessoa [M/F]: ")).upper()
if sexo == 'M':
    print("Voce selecionou o sexo Masculino.")
    peso = 72.7 * altura - 58
    print(f"O seu peso ideal é {peso}")
elif sexo == 'F':
    print("Voce selecionou o sexo Feminino.")
    peso = 62.1*altura - 44.7
    print(f"O seu peso ideal é {peso}")
else:
    print("Sexo invalido, tente novamente")
