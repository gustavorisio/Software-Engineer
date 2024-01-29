#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
#A media de idade do grupo
#Qual é o nome do homem mais velho
#Quantas mulheres tem menos de 20 anos]
somaidade = 0
media = 0
menor_20 = 0
maioridade = 0
nome_velho = ''
cont = 0
for p in range(1,5):
    sexo = str(input("Digite o sexo: [M] ou [F]: ")).upper()
    if sexo == 'M':
        print("Você definiu como sexo MASCULINO.")
        nomeM = str(input("Digite o nome: ")).upper()
        idadeM = int(input("Digite a idade: "))
        somaidade = somaidade + idadeM
        if p == 1:
            maioridade = idadeM
            nome_velho = nomeM
        if idadeM > maioridade:
            maioridade = idadeM
            nome_velho = nomeM           
    elif sexo == 'F':
        print("Você definiu como sexo FEMININO.")
        nomeF = str(input("Digite o nome: ")).upper()
        idadeF = int(input("Digite a idade: "))
        somaidade = somaidade + idadeF
        if idadeF < 20:
            cont = cont + 1
    else: 
        print("Sexo invalido. Tente novamente.")
media = somaidade / 4
print(f"A média dos dois sexos é: {media}")
print(f"O nome do homem mais velho é: {nome_velho}")
print(f"{cont} mulheres são menores de 20 anos. ")