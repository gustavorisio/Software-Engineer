#Faça um algoritmo
#que receba o número de horas trabalhadas e o valor do salário mínimo. Calcule e 
#mostre o salário a receber seguindo as regras abaixo: 
# a. o valor da hora trabalhada vale a metade do salário mínimo; 
# b. o salário bruto equivale ao número de horas trabalhadas multiplicado pelo 
# valor da hora trabalhada; 
# c. o imposto equivale a 3% do salário bruto; 
# d. o salário a receber equivale ao salário bruto menos o imposto.
horas = int(input("Digite as horas trabalhadas: "))
salario = int(input("Digite o valor do salario minimo: "))
a = (salario/2)
b = horas * horas
c = salario + salario * 3/100
d = b - b * 3/100
