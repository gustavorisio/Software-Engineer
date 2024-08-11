salario = int(input("Digite o salario do funcionario: R$"))
print(f"O salario digitado do funcionario é: R${salario}")
if salario >1250:
    aumento = salario + salario*15/100
    print(f"O salario do funcionario com um aumento de 10% é: {aumento}")
if salario <=1250:
    aumento = salario + salario*15/100
    print(f"O novo salario do funcionario com um aumebnto de 15% atualizado: {aumento}")
