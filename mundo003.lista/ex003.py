valores = list()
for _ in range (0,5) :
    valores.append(int(input("Me informe alguns valores :")))
print(valores)
for i in range(len(valores)):
        indice_max = i 
        for j in range (i + 1 , len(valores)):
            if valores[j] < valores[indice_max]:
                indice_max = j

            valores[i],valores[indice_max] = valores[indice_max],valores[i]
print("Lista ordenada em maior e menor :")
print(valores)


