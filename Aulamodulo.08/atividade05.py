import random
aluno1=str(input("Nome do aluno 1 :"))
aluno2=str(input("Nome do aluno 2:"))
aluno3=str(input("Nome do aluno 3:"))
aluno4=str(input("Nome do aluno 4:"))
ordem = [aluno1,aluno2,aluno3,aluno4]
random.shuffle(ordem)
print("os alunos sorteados foram{},".format(ordem))