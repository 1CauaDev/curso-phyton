import random
usuario = int(input("Digite um numero de 1 a 5:"))
num=random.randint(1,5)
print(num)
if usuario == num:
    print("Parabens voce acertou!")
else:
    print("Voce errou, tente novamente!")
    
