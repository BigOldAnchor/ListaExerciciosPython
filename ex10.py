x = float(input("Insira o valor do primeiro número: "))
y = float(input("Insira o valor do segundo número: "))
diferenca = None

if x > y:
    diferenca = x - y
elif y > x:
    diferenca = y - x
else:
    print("Não há diferenças entre os números: ")

print("Diferença entre os dois números: ", diferenca)