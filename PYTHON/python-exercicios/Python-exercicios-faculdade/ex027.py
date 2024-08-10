#Na declaração de imposto de renda devem constar os dados: nome do 
#contribuinte, CPF, renda anual e número de dependentes. Os cálculos são feitos da forma a seguir. 
# Desconto de R$ 110,00 por dependente.
#Com base na renda líquida (renda anual menos descontos) é calculada a alíquota de contribuição de acordo com a tabela:
#  Renda Líquida Alíquota (%)
#  Até R$ 800,00 Isento
#  De R$ 801,00 até R$ 4.000,00 2.5
#  De R$ 4.001,00 até R$ 9.000,00 5
#  Acima de R$ 9.000,00 10
#Elabore o fluxograma para calcular o valor do imposto (Renda Líquida * Alíquota) a ser pago por um contribuinte.]
nome = str(input("Digite o nome do contribuente: "))
CPF = int(input("Digite o CPF: "))
renda_anual = int(input("Digite a renda anual: "))
dependentes = int(input("Quantas pessoas moram com voce? "))
desconto = 110 * dependentes
renda_desconto = renda_anual - desconto 
if renda_desconto < 801:
    print("ISENTO!")
elif renda_desconto >= 801 and renda_desconto <= 4000:
    aliquota = 2.5/100
    final = renda_desconto * aliquota
    print(f"O valor final é R${final}")
elif renda_desconto >=4001 and renda_desconto <= 9000:
    aliquota = 5/100
    final = renda_desconto * aliquota
    print(f"O valor final é R${final}")
elif renda_desconto >=9000:
    aliquota = 10/100
    final = renda_desconto * aliquota
    print(f"O valor final é R${final}")