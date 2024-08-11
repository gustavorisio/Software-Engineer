#Crie um algoritmo que leia um salario e aumente 15% e mostre o novo salario.
salario = int(input("Digite o salario do funcionario: "))
nsalario = salario + (salario * 15/100)
print(f"O salario digitado do funcionario é de {salario}, com 15% de aumento o novo salario é de {nsalario}")