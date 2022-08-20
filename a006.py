#  função para inteiros -- int()  --  7, -4, 0, 9875
#  função para reais -- float()  --  4.5, 0.076, -15.223, 7.0
#  função para boleanos -- bool()  --  True, False
#  função para strings -- str()  --  "Olá", "7.5", ""

#  função para variáveis -- type()  -- retorna o tipo da variável

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
s = n1 + n2

print(type(s))
print("")
print("O resultado é", s)
print("O resultado é {}".format(s))
print("")
print("A soma entre", n1, "e", n2, "vale", s)
print("A soma entre {} e {} vale {}".format(n1, n2, s))
print("A soma entre {0} e {1} vale {2}".format(n1, n2, s))

#  {} chaves duplas é utilizado como uma mascara em python

n = input("Digite um valor: ")
print("Condições")
print("Número: ", n.isnumeric())
print("Alfabético: ", n.isalpha())
print("Alfanúmerico: ", n.isalnum())