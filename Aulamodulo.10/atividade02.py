velocidade = float(input("Digite a velocidade do seu carro:"))
if velocidade > 80 :
    multa = (velocidade -80)*7
    print("Voce foi multado! O valor da multa é de R${:.2f}".format(multa))
print("Tenha um bom dia! Dirija com segurança!")