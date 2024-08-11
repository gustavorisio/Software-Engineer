import math
angulo = float(input("Digite um angulo para descobrir o seu seno, cosseno e tangente: "))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print(f"O valor de angulo {angulo} em seno é: {seno}, em cosseno: {cosseno} e sua tangente: {tangente} ")
