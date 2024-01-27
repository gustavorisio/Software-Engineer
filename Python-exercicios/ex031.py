km = int(input("Digite quantos kilometros o veiculo irá percorrer: "))
if km <= 200:
    passagem = km * 0.50
    print(f"O preço da passagem por percorrer {km} é de: {passagem}.")
else:
    passagem = km * 0.45
    print(f"Para viagens mais longas, o preço da passagem por percorrer {km} é de: {passagem}.")