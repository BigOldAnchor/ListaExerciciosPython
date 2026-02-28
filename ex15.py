import math

cateto1 = int(input("Digite o valor do 1o cateto: "))
cateto2 = int(input("Digite o valor do 2o cateto: "))

hipQuadrada = cateto1 ** 2 + cateto2 ** 2
hipotenusa = math.sqrt(hipQuadrada)

print("Hipotenusa: ", hipotenusa)