ano = int(input("Digite o ano que voce nasceu:"))
idade = 2025 - ano
if idade < 9 :
    print(" Voce tem {} anos e esta na categoria MIRIM".format(idade))
elif idade <= 14 :
    print("Voce tem {} anos e esta na categoria INFANTIL".format(idade))
elif idade <= 19 :
    print("Voce tem {} anos e esta na categoria JUNIOR ".format(idade))
elif idade <= 25 :
    print("Voce tem {} anos e esta na categoria SENIOR".format(idade))
else :
    print("Voce tem {} anos e esta na categoria MASTER".format(idade))
    
print("FIM DO PROGRAMA!")
    