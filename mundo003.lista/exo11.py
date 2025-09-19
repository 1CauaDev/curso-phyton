import random 



print("------------------------------------------")
print("              JOGO DA MEGA-SENA           ")
print("------------------------------------------")
quantidade_jogos = int(input("Quantos jogos voce quer que eu sorteie:"))
for i in range (quantidade_jogos):
     jogo = random.sample(range(1,61),6)
     jogo.sort()

     print(f"Jogo °{i+1} {jogo}")
print("-------------->>>>> BOA SORTE <<<<<-------")

