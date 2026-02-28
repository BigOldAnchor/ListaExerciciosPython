tmpPercurso = int(input("Digite o tempo de percurso (horas): "))
veloMedia = int(input("Digite a velocidade média: "))

distPercorrida = veloMedia * tmpPercurso
ltsGastos = distPercorrida / 12

print("Litros gastos: ", ltsGastos)
