#Escreva um algoritmo que determine o grau de obesidade de uma pessoa, sendo 
#fornecido o peso e a altura da pessoa. O grau de obesidade é determinado pelo 
#índice da massa corpórea (Massa = Peso / Altura2 ) através da tabela abaixo:
#MASSA CORPÓREA GRAU DE OBESIDADE
# < 26 Normal
# >= 26 e < 30 Obeso
# >= 30 Obeso Mórbido
peso = float(input("Digite o peso da pessoa para descobrir seu IMC: "))
altura = float(input("Digite a altura: "))
IMC = peso / altura * altura
if IMC > 26:
    print("Você está com o peso normal.")
elif IMC >= 26 and IMC < 30:   
    print("Você está acima do peso, OBESIDADE!")
elif IMC >=30:
    print("Você está com OBESIDADE MÓRBIDA! CUIDADO!")
print(f"O seu IMC é de {IMC}")

