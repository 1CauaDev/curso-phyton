valores = []
while True :
    valor = int(input("Me informe um valor :"))
    
    if valor in valores :
        print("Valor repetido! Nao vou adicionar ")
    else :
        valores.append(valor)
        print("Valor adicionado com sucesso !")

    resposta = input("Voce deseja continuar ? [S/N]:".strip().lower())
    while resposta not in ['s','n'] :
        resposta = input("Resposta errada digite apenas [S/N]".strip().lower())

    if resposta == 'n' :
        break

valores.sort ()
print()
print(f"Valores digitados em ordem crescentes sao : {valores}")
