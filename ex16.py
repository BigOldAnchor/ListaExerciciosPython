hrsTrabalhadas = int(input("Digite as horas trabalhadas: "))
vlrHora = float(input("Digite o valor da hora: "))
prcDesconto = int(input("Digite o valor percentual de desconto: "))
nmrDescendentes = int(input("Digite o número de descendentes: "))

slrBruto = hrsTrabalhadas * vlrHora
slrLiquido = slrBruto - (slrBruto * prcDesconto / 100) + (100 * nmrDescendentes)

print("Salário bruto: ", slrBruto)
print("Salário líquido: ", slrLiquido)
