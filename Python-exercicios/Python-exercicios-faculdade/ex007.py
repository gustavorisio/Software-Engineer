#Criar um algoritmo (Fluxograma) que converta segundos em minutos e segundos. 
#Por exemplo, 252 segundos equivalem a 4 minutos e 12 segundos.
n = int(input("Digite segundos para ser convertido para minutos e segundos: "))
segundos = n % 60
minutos = n // 60
print(f"{n}segundos são equivalente a {minutos} minutos e {segundos} segundos.")