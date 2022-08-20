produto = str(input("Insira o nome do produto: "))
valor = float(input("Insira o preço do produto: "))
print("O produto {} que custa {:.2f}, custará {:.2f} com 5% de desconto".format(produto, valor, valor*0.95))