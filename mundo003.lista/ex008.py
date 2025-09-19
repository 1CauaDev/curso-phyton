valores = []
par = []
impar = []
for _ in range (0,7):
    num = int(input("Me informe 7 elementos :"))
    valores.append(num)
    if num % 2 == 0 :
        par.append(num)
    else :
        impar.append(num)

par.sort()
impar.sort()

print("-------------------------------------------------------")
print("                         MENU                          ")
print(f"Todos os valores digitados :{sorted(valores)}")
print(f"Número pares em ordem crescente : {par}")
print(f"Os numeros pares em ordem crescente {impar}")
    
