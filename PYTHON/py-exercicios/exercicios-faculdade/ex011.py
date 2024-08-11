#Pedro comprou um saco de ração com peso em quilos. Pedro possui dois gatos 
#para os quais fornece a quantidade de ração em gramas. Faça um algoritmo 
#que receba o peso do saco de ração e a quantidade de ração fornecida para cada gato por dia. Calcule e mostre quanto restará de ração no saco após cindo dias.
peso = int(input("Digite o peso do saco de ração em kg: "))
quantidade = int(input("Digite a quantidade fornecida em gramas para cada gato por dia: "))
resultado = peso / quantidade * 2
restara = peso - (resultado * 5)
print(f"Por dia os dois gatos consomem: {resultado} gramas: ")
print(f"Em 5 dias o saco de ração terá: {restara}kg")