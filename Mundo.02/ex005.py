nome=str(input("Digite seu nome:"))
print("Seja Bem vindo(a) {}!".format(nome))
nota1=float(input("Digite a primeira nota:"))
nota2=float(input("Digite a segunda nota:"))
media=(nota1+nota2)/2
if media < 5.0:
    print("Ola {}, sua media foi {:.1f} voce esta REPROVADO!".format(nome,media))
elif 5.0 <= media <= 6.9:
    print("ola {}, sua media foi {:.1f} voce esta de RECUPERAÇAO!".format(nome,media))
else:
    print("Ola {}, sua media foi {:.1f} voce esta APROVADO!".format(nome,media))
    print("FIM DO PROGRAMA!")