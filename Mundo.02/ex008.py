import random
pedra="pedra"
papel="papel"
tesoura="tesoura"
itens=[pedra,papel,tesoura]
pc=random.choice(itens)
jogador=str(input("pedra,papel ou tesoura:"))
print("O computador escolheu {}".format(pc))
if pc == jogador:
    print("EMPATE")
elif pc == pedra and jogador == papel:
    print("JOGADOR VENCEU")
elif pc == pedra and jogador == tesoura:
    print("PC VENCEU")
elif pc == papel and jogador == pedra:
    print("PC GANHOU")
elif pc ==papel and jogador == tesoura:
    print("JOGADOR WIN")
elif pc == tesoura and jogador == papel:
    print("PC VENCEU")
elif pc == tesoura and jogador == pedra:
    print("JOGADOR VENCEU")
print("FIM DO JOKENPO")