#Faça um programa que peça para informar a quantidade de dinheiro na carteira e calcule com o dolár atual quanto será convertido.
dinheiro = float(input("Quanto de dinheiro voce tem na carteira para ser convertido em dólar? (Cotado atualmente a $4,80)"))
dolar = dinheiro / 4.80
print(f"Voce tem um saldo de {dinheiro}, pode comprar ${dolar} doláres.")