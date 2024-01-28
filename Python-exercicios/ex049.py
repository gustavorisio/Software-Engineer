#Refaça o DESAFIO ex009, mostrando a tabuado de um numero que o usuario escolher, 
# só que agora utilizando um FOR {} IN RANGE
n = int(input("Digite um numero qualquer para ser visualizado a tabuada dele. "))
for t in range(1,11):
    resultado = n * t 
    print(f"{n} x {t} = {resultado}")