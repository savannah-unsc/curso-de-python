#  frase = "Curso em Vídeo Python"   --   Cadeia de Caracteres
#  frase[9]  --  Identifica apenas o caractere 9
#  frase[9:13]  --  Identifica apenas os caracteres entre 9 e 12
#  frase[9:21]  --  Identifica apenas os caracteres entre 9 e 20
#  frase[9:21:2]  --  Identifica apenas os caracteres entre 9 e 20 pulando 1 caractere
#  frase[:5]  --  Identifica apenas os caracteres entre 0 e 4
#  frase[15:]  --  Identifica apenas os caracteres entre 15 e 20
#  frase[9::3]  --  Identifica apenas os caracteres entre 9 e 20 pulando 2 caracteres

#  len(frase)  --  Devolve o comprimento da frase
#  frase.count("o")  --  Conta quantas vezes existe a letra "o"
#  frase.count("o", 0, 13)  --  Conta quantas vezes existe a letra "o" entre os caracteres 0 e 12
#  frase.find("deo")  --  Mostra o ínicio de uma parte da String
#  frase.find("Android")  --  Caso não exista essa parte em sua String o valor retornado será -1
#  "Curso" in frase  --  Retorna um valor boleano
#  frase.replace("Python", "Android")  -- Substitui "Python" por "Android"

#  frase.upper()  --  Deixa a frase em letras maiúsculas
#  frase.lower()  --  Deixa a frase em letras minúsculas
#  frase.capitalize()  --  Deixa a frase capitalizada (com apenas a primeira letra da String maiúscula)
#  frase.title()  --  Deixa a frase com todas as primeiras letras de palavras em maiúsculo

#  frase = "   Aprendendo Python  "
#  frase.strip   --  Remove todos os espaços no começo e final da String
#  frase.rstrip   --  Remove todos os espaços no final da String
#  frase.lstrip   --  Remove todos os espaços no começo da String

#  frase = "Curso em Vídeo Python"   --   Cadeia de Caracteres
#  frase.split()  --  Divide a String onde estiver espaços à transformando em uma lista
#  "-".join(frase)  --  Junta a lista utilizando "-" como espaçador


frase = "Curso em vídeo Python"
print(frase[::2])

print("Oi")

#  Imprime o texto exatamente como está entre as """"""
print("""
A felicidade aparece para aqueles que reconhecem a importância das pessoas que passam em nossa vida.
Não sei amar pela metade, não sei viver de mentiras, não sei voar com os pés no chão.
Amar não acaba. É como se o mundo estivesse a minha espera. E eu vou ao encontro do que me espera.
Cada vez mais acho tudo uma questão de paciência, de amor criando paciência, de paciência criando amor.""")