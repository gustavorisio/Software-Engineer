#Faça um algoritmo que receba o custo de um espetáculo teatral e o preço do convite deste espetáculo. 
#Esse algoritmo deve calcular e mostrar a quantidade de convites que devem ser vendidos para que pelo menos o custo do espetáculo seja alcançado.
custo = int(input("Digite o valor de custo do espataculo teatral: R$"))
convite = int(input("Digite o valor do convite: R$"))
quantidade = custo  / convite
print(f"O numero de convites que devem ser vendidos para alcançar o custo do espetaculo é: {quantidade} convites.")