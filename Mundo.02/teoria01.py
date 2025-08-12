nome = str(input("Digite seu nome :"))
if nome == 'Gustavo':
    print("QUE NOME LINDO VOCE TEM!")
elif nome == 'Pedro' or nome == 'maria' or nome == 'Paulo':
    print("Seu nome é bem popular no brasil!")
elif nome in 'Jasmim valdilene maria':
    print("Belo nome feminino!")
else:
    print("Seu nome é bem normal!")
print("Bom dia,{}!".format(nome))
 