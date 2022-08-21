#  import math  -- Importa uma biblioteca por completo
#  from math import factorial  --  Importa apenas uma função de uma biblioteca
#  from math import factorial, sqrt


from math import sqrt
import random
import emoji

num = int(input("Digite um número: "))
raiz2 = sqrt(num)

print("A raiz quadrada de {} é igual a {:.2f}".format(num, raiz2))

random = random.randint(1, 10)
print("O número aleatório gerado foi {}".format(random))

print(emoji.emojize("Olá, Mundo! :earth_americas:", language="alias"))