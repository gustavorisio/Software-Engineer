#Um programa que mostra o tipo do que foi digitado pelo usuario
leia = input("Digite algo para identificar o tipo escrito: ")
print ("O tipo primitivo lido é:", type(leia))
print ("Só tem espaços? ", leia.isspace())