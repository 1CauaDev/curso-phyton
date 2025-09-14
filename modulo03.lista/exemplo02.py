valores = list()
for cont in range(0,5) :
    valores.append(int(input("Digite um valor :")))
#valores.append (5)
#valores.append (9)
#valores.append (4)

for c ,valor in enumerate (valores):
    print(f'na posiçao {c}° encontrei o valor {valor}!')
print('cheguei no final da lista.')
#usando for e append e como inserir numeros para lista 