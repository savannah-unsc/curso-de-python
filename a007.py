#  5 + 2 == 7  --  Soma
#  5 - 2 == 3  --  Subtração
#  5 * 2 == 10  --  Multiplicação
#  5 / 2 == 2.5  --  Divisão Completa
#  5 ** 2 == 25  --  Potênciação
#  5 // 2 == 2  --  Divisão Inteira
#  5 % 2 == 1  --  Resto de Divisão


#  Ordem de Precedência

#  1-  ()
#  2-  **
#  3-  *, /, //, %
#  4-  +, -

#  5+3*2 == 11
#  3*5+4**2 == 31
#  3*(5+4)**2 == 243


nome = str(input("Qual o seu nome? "))
#  > alinha a esquerda
#  < alinha a direita
#  ^ Centraliza
#  (caractere) preenche o espaço
print("Prazer em te conhecer {:~^20}!".format(nome))

n1 = int(input("Digite um valor: "))
n2 = int(input("Digite outro valor: "))
print("A soma entre {} e {} é {}".format(n1, n2, n1+n2))
print("A subtração entre {} e {} é {}".format(n1, n2, n1-n2))
print("A multiplicação entre {} e {} é {}".format(n1, n2, n1*n2))
print("A divisão entre {} e {} é {:.3f}".format(n1, n2, n1/n2))
print("O resultado de {} elevado a {} é {}".format(n1, n2, n1**n2))
print("A divisão inteira entre {} e {} é {}".format(n1, n2, n1//n2))
print("O resto da divisão entre {} e {} é {}".format(n1, n2, n1%n2))

#  :.3f  --  deixa o número real com apenas 3 casas após o ponto
#  end=""  --  Faz a função print() não quebrar a linha após seu termino
#  \n  -- Quebra a linha