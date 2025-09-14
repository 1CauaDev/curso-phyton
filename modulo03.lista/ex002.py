valores = []
repetidos = []
for _ in range (0,1000) :
    num = int(input("Digite um numero:"))
    valores.append(num)
    
    if len(valores) >= 2 and valores[-1] == valores[-2]:
        print("Numero repetido consecutivamente. Encerrado...")
        break
    print()
    
for n in valores:
    if valores.count(n) > 1 and n not in repetidos:
        repetidos.append(n)
        
    
    
print("Lista final:",valores)
print(f"A quantidade de elementos foram: {len(valores)}")
print(f"o numero repetido :{repetidos}")
  
    

