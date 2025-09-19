boletim = []
while True:
    alunos = str(input("Nome:"))
    nota1 = float(input("Nota 1:"))
    nota2 = float(input("Nota 2 :"))

    media = (nota1 + nota2)/2

    boletim.append([alunos,nota1,nota2,media])

    resposta = input("Voce deseja continuar ? [S/N]:".strip().lower())
    while resposta not in ['s','n'] :
        resposta = input("Resposta errada, digite [S/N]:".strip().lower())

    if resposta == 'n' :
        break

print("-----------------boletim--------------------------------")
print(f"{'ALUNO':<15}{'NOTA(1)':<10}{'NOTA(2)':<10}{'MEDIA':<6}")
print("--------------------------------------------------------")
for aluno in boletim :
    print(f"{aluno[0]:15}{aluno[1]:<10.1f}{aluno[2]:<10.1f}{aluno[3]:<6.1f}")

