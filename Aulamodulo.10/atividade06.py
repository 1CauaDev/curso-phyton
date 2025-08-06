num1 = int(input("Me informe o primeiro numero:"))
num2 = int(input("Me informe o segundo numero:"))
num3 = int(input("Me informe o terceiro numero:"))
if num1 >= num2 and num1 >= num3:
    maior = num1
if num2 >= num1 and num2 >= num3:
    maior = num2
if num3 >= num1 and num3 >= num2:
    maior = num3 
    print("O maior numero é {}".format(maior))
    if num1 <= num2 and num1 <= num3:
        menor = num1
    if num2 <= num1 and num2 <= num3:
        menor = num2
    if num3 <= num1 and num3 <= num2 :
        menor = num3
    print("O menor numero é {}".format(menor))
print("FIM DO PROGRAMA!")