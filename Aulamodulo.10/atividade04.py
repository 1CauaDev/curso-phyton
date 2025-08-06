viagem = int(input("Me informe a distancia da sua viagem em Km:"))
if viagem <= 200:
    preco = viagem * 0.50
else:
    preco = viagem * 0.45
print(" O valor da sua passagem é R${:.2f}".format(preco))
print("Tenha uma boa viagem!")