
print("BEM VINDO A MATEMATICA INTELIGENTE!")
print("[1] SOMAR")
print("[2] SUBTRAIR")
print("[3] Multiplicar")
print("[4] Sair")
opcao = int(input("Escolha uma opcao:"))
if opcao == 1 :
        num1=int(input("Me informe o primeiro valor:"))
        num2=int(input("Me informe o segundo valor :"))
        soma = num1 + num2 
        print("O resultado da soma de {} + {} = {}".format(num1,num2,soma))
elif opcao == 2 :
        valor1 = int(input("Me informe o primeira valor:"))
        valor2 = int(input("Me informe o segunda valor:"))
        subt = valor1 - valor2 
        print("O resultado da subtraçao de {} - {} = {}".format(valor1,valor2,subt))
elif opcao == 3 :
        n1 = int(input("Me informe o primeiro numero:"))
        n2 = int(input("Me informe o segundo numero:"))
        mult = n1 * n2 
        print("A multiplicaçao de {} * {} = {}".format(n1,n2,mult))
elif opcao == 4:
        print("SAIR DO PROGRAMA...")
    