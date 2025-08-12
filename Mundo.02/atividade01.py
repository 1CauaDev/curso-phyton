casa=float(input("Qual o valor da casa? R$").replace(',',',').replace('.' , '.'))
salario=float(input("Qual o seu salario Mensal? R$").replace(',',',').replace('.' , '.'))
anosaluguel=int(input("Em quantos anos voce pretende pagar?"))
prestacao = casa / (anosaluguel * 12)
if prestacao <= salario * 0.30:
    print("Emprestimo aprovado!")
else:
    print("emprestimo negado!")
    print("A prestacao mensal seria de R${:.2f}".format(prestacao))
print("FIM DO PROGRAMA!")