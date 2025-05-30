produto = float(input(" Me informe o preço do Produto R$:"))
valor_do_desconto = float(produto) * 0.05
valor_do_produto = float(produto) - 0.60
print("o valor do desconto foi {:.2f} % ".format(valor_do_desconto))
print("o valor do produto foi {:.2f} R$ ".format(valor_do_produto))