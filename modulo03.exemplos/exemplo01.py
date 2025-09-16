num = [2,3,7,5]
num[2] = 3
num.append(7) 
num.sort(reverse=True)
num.insert(2,2)
if 5 in num :
    num.remove(5)
else :
    print('Nao achei o numero 4 ')
print(num)
print(f'Essa lista tem {len(num)} elementos')
#inserindo numero na lista e removendo,colocando em ordem , e inserindo 
#o LEN usado para mostrar quantos numeros 
