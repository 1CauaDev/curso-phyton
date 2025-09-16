valores = []
while True :
    valor = int (input("Me informe um valor :"))
    valores.append(valor)
    print()

    resposta = input("Voce deseja continuar [S/N]:".upper().lower())
    while resposta not in ('s','n') :
        resposta = input("Digitado Errado , Digite apenas [s/n]".strip().lower())

    if resposta == 'n' :
        break
    
    print()

pares = []
impares = []
for num in valores :
    if num % 2 == 0 :
        pares.append(num)
    else :
        impares.append(num)
print(f"Os valores da lista foram {valores}")
print(f"Os valores pares sao {pares}")
print(f"os valores impares sao {impares}")


