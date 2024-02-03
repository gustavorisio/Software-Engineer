#João recebeu seu salário e precisa pagar duas contas que estão atrasadas. Como as 
#contas estão atrasadas, João terá que pagar multa de 2% sobre cada conta. Faça 
#um algoritmo (Fluxograma) que calcule e mostre quanto restará do salário do João.
salario = int(input("Digite o salario do joao: "))
novosalario = salario - salario * 4/100
multa = salario * 4/100
print(f"A multa que o João terá que pagar é R${multa} e o novo salario de João é R${novosalario}")