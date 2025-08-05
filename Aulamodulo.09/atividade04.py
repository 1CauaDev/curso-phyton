frase =str(input("Digite uma frase qualquer:"))
print("A letra A aparece {} vezes na frase.".format(frase.lower().count('a'))) 
print("A primeira letra A aparece na posicao {}.".format(frase.find('a')))
print("A ultima Letra A aparece na posiçao {}.".format(frase.rfind('a')))
