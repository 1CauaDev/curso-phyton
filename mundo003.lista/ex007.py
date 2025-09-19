dados = []
totmai = totmen = 0 
while True :
    nome = str(input("Nome :"))
    peso = int(input("peso :"))
    dados.append([nome,peso])




    resposta = input("Voce deseja continuar ? [S/N]:".strip().lower())
    while resposta not in ['s','n'] :
            resposta = input("Resposta digitada errada , somente  [s/n]:".strip().lower())

    if resposta == 'n' :
     break
for pos, item in enumerate (dados) :
    nome =item[0]
    peso = item[1]
    print(f"Posiçao: {pos}| Nome:{nome} | Peso:{peso} KG")

maior = max(dados, key=lambda x: x[1])
menor = min(dados, key=lambda x: x[1])

print(f"maior  peso: {maior[1]} KG - Nome: {maior[0]}")
print(f"menor peso: {menor[1]} KG - Nome: {menor[0]}")
