

dados = []
while True :
    nome = str(input("Nome :"))
    peso = str(input("peso :"))
    dados.append([nome,peso])




    resposta = input("Voce deseja continuar ? [S/N]:".strip().lower())
    while resposta not in ['s','n'] :
            resposta = input("Resposta digitada errada , somente  [s/n]:".strip().lower())

    if resposta == 'n' :
     break

for pos, item in enumerate (dados) :
    nome =item[0]
    peso = item[1].replace("Kg","")
    print(f"Posiçao: {pos}| Nome:{nome} | Peso:{peso} KG")
