#Criar um algoritmo (Fluxograma e Pseudocódigo) que receba o salário de um 
#funcionário e o percentual de aumento, calcule e mostre o valor do aumento e o novo salário.
salario = int(input("Digite o salario do funcionario: "))
percentual = int(input("Digite o percentual[%] de aumento do funcionario: "))
aumento = salario + salario * percentual/100
print(f"O novo salario do funcionario é de {aumento}")