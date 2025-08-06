r1 = float (input("Me fala o primeiro comprimento:"))
r2 = float ( input("Me fala o segundo comprimento:"))
r3 = float (input("Me fala o terceiro comprimento:"))
if r1 < r2 + r3 and r2 <r1 + r3 and r3 < r1 + r2 :
    print("Os segmentos podem formar um triangulo!")
else:
    print("os segmentos nao podem formar um triangulo!")
print("FIM DO PROGRAMA!")
