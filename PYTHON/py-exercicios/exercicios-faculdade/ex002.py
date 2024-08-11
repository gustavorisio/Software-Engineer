#Dados o tamanho de um arquivo (em bits), bem como a velocidade da conexão 
#(em bits por segundo), informe o tempo necessário para o download do arquivo.
bits = int(input("Digite o tamanho do arquivo em bits: "))
velocidade = int(input("Digite a velocidade da internet em bits/s: "))
tempo = bits / velocidade
print(f"Um arquivo de {bits} bits com uma internet de {velocidade} bits/s, o tempo restante para download do arquivo é de: {tempo} segundos.")