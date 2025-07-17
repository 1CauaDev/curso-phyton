import math
an = float(input("Digite o angulo que voce deseja:"))
sen = math.sin(math.radians(an))
print("O angulo de {} tem o SENO de {:.2f}".format(an,sen))
cosseno= math.cos(math.radians(an))
print("O angulo de {} tem o COSSENO de {:.2f}".format(an,cosseno))
tangente = math.tan(math.radians(an))
print("O angulo de {} tem a TANGENTE de {:.2f}".format(an,tangente))