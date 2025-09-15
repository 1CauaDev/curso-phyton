num =int(input("Digite um numero inteiro:"))
opcao = int (input("escolha umas das bases de conversao:"))
print("[1] converter para BINARIO")
print("[2] coverter para octal")
print("[3] converter para hexadecimal")
if opcao == 1:
    print("{} convertido para BINARIO é igual a {}".format(num,bin(num)[2:]))
elif opcao == 2:
    print("{} convetido para octal é igual a {}".format(num,oct(num)[2:]))
elif opcao ==3: 
    print("{} convertdido para hexadecimal é igual a {}".format(num,hex(num)[2:]))
else:
    print("opcao invalida")
    print("FIM DO PROGRAMA!")



