#Crie um programa que leia dois valores e mostre um menu como ao lado na tela:
#Seu programa deverá realizar a operação solicitada em cada caso.
#[1] SOMAR
#[2] MULTIPLICAR
#[3] MAIOR
#[4] NOVOS NUMEROS
#[5] SAIR DO PROGRAMA
terminar = False
while not terminar:
    n1 = int(input("Digite um valor: "))
    n2 = int(input("Digite outro valor: "))
    print("""Selecione uma opção:
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NUMEROS
    [5] SAIR DO PROGRAMA""")
    opção = int(input("Selecione uma opção: "))
    if opção == 1:
        soma = n1+n2
        print(f"O resultado da soma dos dois valores é: {soma}")
    elif opção == 2:
        multiplicar = n1 * n2
        print(f"O resultado da multiplicação dos dois valores: {multiplicar}")
    elif opção == 3:
        if n1 > n2:
            print(f"O numero {n1} é maior que o numero {n2}")
        elif n2 > n1:
            print(f"O numero {n2} é maior que o numero {n1}")
    elif opção == 4:
        print("""Selecione uma opção:
        [1] SOMAR
        [2] MULTIPLICAR
        [3] MAIOR
        [4] NOVOS NUMEROS
        [5] SAIR DO PROGRAMA""")
        n1 = int(input("Digite um novo valor: "))
        n2 = int(input("Digite novmaente outro valor: "))
    elif opção == 5:
        terminar = True
    else:
        print(f"Opção invalida, tente novamente")
print("Fim do programa!")
    
        
        
    