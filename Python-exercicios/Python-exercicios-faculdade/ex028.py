#Criar um algoritmo (Fluxograma) que peça para o usuário informar uma letra 
#qualquer. No final do processamento, o programa deverá informar se a letra é vogal ou consoante
letra = str(input("Digite uma letra "))
if letra in ['a', 'e','i','o','u']:
    print("A letra é uma vogal.")
else:  
    print("A letra é uma consoante")