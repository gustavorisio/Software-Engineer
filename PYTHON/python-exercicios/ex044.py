#Elabore um programa que calcule o valor a ser pago por um produto.
#Considerando o seu preço normal e condiçã de pagamento:
#A vista dinheiro = 10% desconto
#A vista no cartão = 5% de desconto
#em até 2x no cartão = preço normal
#3x ou mais no cartão = 20% de juros
valor = int(input("Digite o valor total: R$"))
print(f"O valor das compras é de R${valor}.")
print("====================================")
print("""Escolha uma forma de pagamento:
[1] A vista dinheiro 
[2] A vista no cartão
[3] 2x sem juros no cartão
[4] 3x ou mais no cartão com juros""")
print("====================================")
opção = int(input("Digite a opção desejada: "))
if opção == 1:
    dinheiro = valor - (valor * 10/100)
    print(f"O valor R${valor}, com 10% de desconto a vista no dinheiro: R${dinheiro}.")
elif opção == 2:
    cartao = valor - (valor * 5/100)
    print(F"O valor R${valor}, com 5% de desconto a vista no cartão: R${cartao}.")
elif opção == 3:
    cartao2x = valor / 2
    print(f"O valor R${valor} em 2x no cartão é de R${cartao2x}")
elif opção == 4:
    parcelas = int(input("Digite quantas vezes quer parcelar no cartão de crédito:"))
    total = valor + (valor * 20/100)
    mensal = total / parcelas
    print(f"O valor total R${total} em {parcelas}x com juros, o valor a ser pago por mês: R${mensal}")
else:
    print("Opção de forma pagamento invalida.")
