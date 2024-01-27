#Escreva um programa para aprovar o emprestimo bancario de uma casa. 
#O programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar. 
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salario ou então o emprestimo será negado.
from time import sleep
casa = int(input("Digite o valor da casa que tem interesse. "))
salario = float(input("Digite o seu salario para calcular. "))
anos = int(input("Quantos anos de financiamento? "))
print("Analisando....")
sleep(2)
meses = anos * 12
prestacao = casa / (anos * 12) 
minimo = salario * 30/100
print(f"Para pagar uma casa de R${casa} com o seu salario de R${salario}")
print(f"Você deverá pagar prestações de R${prestacao} por {meses} meses.")
print(f"O minimo para ser aprovado o emprestimo é de R${minimo} ou 30% do seu salario.")
if prestacao <= minimo:
    print("O emprestimo foi aprovado!")
else:
    print("O emprestimo foi negado.")