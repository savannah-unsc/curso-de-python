reais = float(input("Insira quantos R$ você tem: "))
dolar = reais * 0.193512493650371
euro = reais * 0.192799136862634
print("Seus R$ {} são equivalentes a:")
print("${:.2f}".format(dolar))
print("€{:.2f}".format(euro))