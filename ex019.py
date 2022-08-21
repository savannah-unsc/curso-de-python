from random import choice

a1 = str(input("Digite o nome do primeiro aluno: "))
a2 = str(input("Digite o nome do segundo aluno: "))
a3 = str(input("Digite o nome do terceiro aluno: "))
a4 = str(input("Digite o nome do quarto aluno: "))

var = choice([a1, a2, a3, a4])

print("O aluno escolhido para apagar o quadro foi {}".format(var))

