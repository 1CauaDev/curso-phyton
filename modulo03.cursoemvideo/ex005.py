produto = ('lapis',1.50,'maleta',10,'bolsa',10.90)
print(produto)
print("-------------------------------------------------------")
print("                  LISTAGEM DE PREÇOS                   ")
print("-------------------------------------------------------")
print("{:.<30} R$ {:>6.2f}".format(produto[0],produto[1]))
print("{:.<30} R$ {:>6.2f}".format(produto[2],produto[3]))
print("{:.<30} R$ {:>6.2f}".format(produto[4],produto[5]))

