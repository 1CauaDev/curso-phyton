ano=int(input("Digite o ano que voce nasceu:"))
idade=2025-ano
if idade <= 17:
    print("Voce nao pode se alistar ainda falta {} anos".format(18-idade))
elif idade == 18:
    print("Voce tem que se alistar esse ano")
else:
    print("Voce ja deveria ter se alsitado a {} anos".format(idade-18))
    print("FIM DO PROGRAMA!")