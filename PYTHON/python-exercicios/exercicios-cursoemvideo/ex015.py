#Escreva um programa que pergunte a quantidade em KM percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado
km = float(input("Digite quantos km o carro percorreu: "))
dias = float(input("Digite quantos dias ele foi alugado: "))
cdias = dias * 60 
ckm = km * 0.15
vaipagar=cdias+ckm
print(f"O veiculo percorreu {km}km gastando R${ckm} em {dias}dias gastando R${cdias} e o valor a ser pago pelo carro alugado é de R${vaipagar}")