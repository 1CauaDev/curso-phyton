expressao = []
while True :
    simb = input("Me informe uma expressao com parenteses :")

    if simb =='':
        break
    if simb not in ('(',')') :
        print("Digite apenas '('ou')' .")
        continue
    expressao.append(simb)

    pilha = []
    for simb in expressao :
        if simb == '(' :
            pilha.append('(')
        elif simb == ')':
            if len(pilha) >0:
                pilha.pop
            else :
                pilha.append(')')
                break

print(f"Expressao digitada foi {expressao}")
if len(pilha) == 0:
    print("Sua expressao esta correta !")
else :
    print("Expressao incorreta !")


