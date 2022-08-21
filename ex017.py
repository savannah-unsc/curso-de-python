from math import hypot

num1 = float(input("Digite o valor do cateto oposto: "))
num2 = float(input("Digite o valor do cateto adjacente: "))
hip = hypot(num1, num2)
print("O triangulo com catetos {} e {} terá a hipotenusa {:.2f}".format(num1, num2, hip))