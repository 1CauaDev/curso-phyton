numeros = []
for _ in range (4):
    numero = int(input("Digite um valor :"))
    numeros.append(numero)
print(numeros)

pares = [n for n in numeros if n % 2 ==0]

if pares :
    print(f"Números pares digitados: {pares}")
else :
    print("Nenhuma numero par foi digitado")
if 3 in numeros :
    print(f"o numero 3 apareceu {numeros.count(3)} vezes e esta na posicao:",end=" " )
else:
        print("o numero 3 nao apareceu nenhuma vez")
for pos,numero in enumerate(numeros):
    if numero == 3:
        print(pos, end="")

if 9 in numeros :
    print(f" ,O numero 9 apareceu {numeros.count(9)} vez(es) ." )
else:
    print("O numero 9 nao apareceu nenhuma vez!")

    

    
    
    
    

 