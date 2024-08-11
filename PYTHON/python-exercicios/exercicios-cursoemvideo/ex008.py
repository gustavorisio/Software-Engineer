#Crie um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros
n = int(input("Digite um valor em metros para ser convertido em centimetros e milimetros: "))
centimetros = n * 100
milimetros = n * 1000
print(f"{n} metros em centimetros: {centimetros}cm e convertido em milimetros {milimetros}mm")