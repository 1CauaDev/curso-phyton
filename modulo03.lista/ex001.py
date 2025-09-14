valores = list()
for cont in range (0,5):
    valores.append(int(input("Digite um valor :")))
print(f' valores digitados :{valores}')

menor = min (valores)
maior = max (valores)

print(f'o menor valor é {menor} e esta na posiçoes:', end='' )
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...', end='')
print()
        
print( f'o maior valor é {maior} e esta na posiçoes:', end='')
for i, v in enumerate(valores):
    if v== maior:
        print(f'{i}...' ,end='')

print()

