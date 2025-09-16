valores = []
while True :
    valor = int(input("Me informe um valor :"))
    valores.append(valor)
    print()

    reposta = input("Voce deseja continuar ? [S/N]: ".strip().lower())
    while reposta not in ['s','n'] :
        reposta = input("Digitado errado , digite apenas [s/n]".strip().lower())

    if reposta == 'n' :
        break
    print()

valores.sort(reverse=True)
print(f"Essa lista tem {len(valores)} elementos")
print(f"Os valores em ordem decrescente ficou {valores}")
if 5 in valores :
        print("O numero 5 esta na lista ")
else :
        print("O numero 5 nao apareceu na lista ")


