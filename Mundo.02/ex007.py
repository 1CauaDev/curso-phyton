opcao = int(input("Qual sera a forma de pagamento? [1] A vista dinheiro/cheque [2] cartao [3] 3x no cartao com juros:"))
preco = float(input("Qual o valor total das compras?R$"))
if opcao == 1:
    total = preco -(preco * 0.10 )
    print("O valor a ser pago é de R${:.2f}".format(total))
elif opcao == 2:
    total = preco -(preco *0.05)
    print("O valor a ser pago é de R${:.2f}".format(total))
elif opcao == 3 :
    total = preco + (preco * 0.20)
    print("O valor a ser pago é de R${:.2f}".format(total))
else:
    print("A Opcao é invalida")
    print("FIM DO PROGRAMA!")