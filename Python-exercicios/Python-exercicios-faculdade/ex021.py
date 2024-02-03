#Faça um algoritmo para calcular a conta final de um hóspede de um hotel fictício, contendo: o nome do hóspede, o tipo do apartamento, o número de diárias 
#utilizadas, o valor unitário da diária, o valor total das diárias, o valor do consumo interno, o subtotal, o valor da taxa de serviço e o total geral. Considere que:
# a. serão lidos o nome do hóspede, o tipo do apartamento utilizado (A, B, C ou D), o número de diárias utilizadas pelo hóspede e o valor do consumo interno do hóspede;
# b. o valor da diária é determinado pela seguinte tabela:
#==================================
#TIPO DO APTO. VALOR DA DIÁRIA (R$)
#A=150,00  B=100,00  C=75,00  D=50,00  o valor total das diárias é calculado pela multiplicação do número de diárias utilizadas pelo valor da diária;
# c. o subtotal é calculado pela soma do valor total das diárias e o valor do consumo interno;
# d. o valor da taxa de serviço equivale a 10% do subtotal;
# e. a total geral resulta da soma do subtotal com a taxa de serviço
nome = str(input("Digite o seu nome: ")).upper()
print("""Digite o tipo de apartamento:
[A] = R$150.00
[B] = R$100.00
[C] = R$75.00
[D] = R$50.00""")
a = 0
opção = str(input(f"Olá, {nome}, escolha uma opção: ")).upper()
if opção == 'A':
    a = 150
    print(f"Você escolheu o apartamento A no valor de R${a}")
elif opção == 'B':
    a = 100
    print(f"Você escolheu o aparamento B novalor de R${a}")
elif opção == 'C':
    a = 75
    print(f"Você escolheu o apartamento C no valor de R${a}")
elif opção == 'D':
    a = 50
    print(f"Você escolheu o apartamento D no valor de R${a}")
else:
    print("Opção invalida, tente novamente!")
diaria = int(input("Digite quantas dias o hospede ficou hospedado: "))
consumo = float(input("Digite quantos R$ o hospedou consumiu: R$"))
subtotal = (a * diaria) + consumo
taxa = subtotal * 10/100
resultado = subtotal + taxa
print(f"O consumo no hotel foi de R${consumo}")
print(f"O hospede terá que pagar um total de R${resultado}")
