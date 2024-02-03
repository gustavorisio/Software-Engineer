#Criar um algoritmo (Fluxograma e Pseudocódigo) que calcule o consumo médio 
#de um automóvel (medido em km/l), dado que são conhecidos a distância total 
#percorrida e o volume de combustível consumido para percorrê-la (medido em litros).
distancia = int(input("Digite a distancia total percorrida pelo automovel em km: "))
volume = int(input("Digite o volume consumido de combustivel em litros: "))
consumo = distancia / volume
print(f"O consumo médio que o automovel consumiu km/l é de {consumo} litros")
