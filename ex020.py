from random import shuffle

a1 = str(input("Digite o nome do primeiro aluno: "))
a2 = str(input("Digite o nome do segundo aluno: "))
a3 = str(input("Digite o nome do terceiro aluno: "))
a4 = str(input("Digite o nome do quarto aluno: "))

lista = [a1, a2, a3, a4]

shuffle(lista)

print("A Ordem de apresentação será: {}, {}, {} e {}".format(lista[0], lista[1], lista[2], lista[3]))