import math

coefA = int(input("Coeficiente A: "))
coefB = int(input("Coeficiente B: "))
coefC = int(input("Coeficiente C: "))

delta = coefB ** 2 - 4 * coefA * coefC

if delta < 0:
    print("Não existem raízes reais.")
else:
    delta = math.sqrt(delta)
    raiz1 = (-coefB + delta) / (2 * coefA)
    raiz2 = (-coefB - delta) / (2 * coefA)
    print("Raízes reais:\n", raiz1, raiz2)
