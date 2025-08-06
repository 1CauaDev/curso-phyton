funcionario = float(input("Digite o salario do funcionario:"))
if funcionario <= 1250:
    aumento = funcionario * 0.15
else:
    aumento = funcionario * 0.10
print("O valor do aumento é de R${}".format(aumento))
print("O novo salario é de R${}".format(funcionario + aumento))
print("FIM DO PROGRAMA!")