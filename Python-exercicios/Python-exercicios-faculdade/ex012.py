#Faça um algoritmo que leia as 3 notas de um aluno e calcule a média 
#final deste aluno. Considerar que a média é ponderada e que o peso das notas é: 
# 2, 3 e 5, respectivamente.
n1 = int(input("Digite a n1 do aluno: "))
n2 = int(input("Digite a n2 do aluno: "))
n3 = int(input("Digite a n3 do aluno: "))
peso1 = 2
peso2 = 3
peso3 = 5
soma_peso = peso1 + peso2 + peso3
media =  n1 * peso1 + n2 * peso2 + n3 * peso3 / soma_peso 
print(f"A media ponderada do aluno é: {media}")