maiores = 0 
for ano in range (1,7+1):
    nasc = int(input(" Em que ano a {} pessoa nasceu?".format(ano)))
    idade = 2025 - nasc
    if idade >= 18:
        maiores +=1
        print("VOCE JA ESTA MAIOR DE IDADE!")
    else:
        print("VOCE AINDA É MENOR DE IDADE!")
print("Quantidade de pessoas maiores de idade: {}".format(maiores))

    