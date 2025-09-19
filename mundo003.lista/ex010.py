matriz = []
valores_pares = []
soma_terceira_coluna = 0
maior_segunda_linha = 0
for i in range (3):
    linha = []
    for j in range (3):
        valor = int(input("Informe elementos para alimentar a matriz :"))
        linha.append(valor)
    matriz.append(linha)

    print("Matiz Digitada!")
    for valor in matriz :
        print(valor)
soma_pares = 0
for linha in matriz :
    for valor in linha :
        if valor % 2 == 0 :
            valores_pares.append(valor)
            soma_pares += valor 
for linha in matriz :
    soma_terceira_coluna += linha[2]

maior_segunda_linha = max(matriz[1])




        

print(f"A soma dos valores pares sao :{soma_pares}")
print(f"Os valores pares que voce adicionou foi {valores_pares}")
print(f"A soma da terceira coluna:{soma_terceira_coluna}")
print("O maior valor da segunda linha é :",maior_segunda_linha)

