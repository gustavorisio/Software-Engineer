aprovados = 0
reprovados = 0
exame = 0

for i in range(5):
    nota1 = float(input(f"Nota 1 do aluno {i+1}: "))
    nota2 = float(input(f"Nota 2 do aluno {i+1}: "))
    
    media = (nota1 + nota2) / 2
    
    if media >= 7.0:
        aprovados += 1
    elif media < 5.0:
        reprovados += 1
    else:
        exame += 1

print(f"\nQuantidade de alunos aprovados: {aprovados}")
print(f"Quantidade de alunos reprovados: {reprovados}")
print(f"Quantidade de alunos em exame: {exame}")
