nome = str(input("Digite seu nome completo: "))
nome = nome.strip()
nomeup = nome.upper()
nomelow = nome.lower()
nometam = len("".join(nome.split()))
pnome = len(nome.split()[0])

print("")
print("Olá {}! Seu nome fica".format(nome))
print("Maiúsculas: {}".format(nomeup))
print("Mainúsculas: {}".format(nomelow))
print("Tamanho Completo: {} caracteres".format(nometam))
print("Tamanho Primeiro Nome: {} caracteres".format(pnome))