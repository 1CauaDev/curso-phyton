import random

numeros = [random.randint(1,10) for _ in range(5)]

print("numeros gerados:", numeros)

menor = min(numeros)
maior =max(numeros)

print(f"o menor valor é {menor}")
print(f"O maior valor é {maior}")



