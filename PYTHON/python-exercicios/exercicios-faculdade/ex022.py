#João Papo-de-Pescador, homem de bem, comprou um microcomputador para 
#controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de 
#peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo 
#(50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa 
#que você faça um Fluxograma que leia a variável P (peso de peixes) e verifique 
#se há excesso. Se houver, gravar na variável E (Excesso) e na variável M o valor 
#da multa que João deverá pagar. Caso contrário mostrar tais variáveis com o 
#conteúdo ZERO.
p = int(input("Digite o peso em quilos: "))
if p > 50:
    excesso = p - 50
    multa = excesso * 4
    print(f"O peso do produto é de {p}, o excesso de peso é: {excesso} gramas. A multa pelo excesso de peso é de R${multa} ")
else:
    print(f"O peso do produto é de {p} gramas, não há excesso. O valor é 0.")