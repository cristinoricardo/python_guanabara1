#19 Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
import random
nro1 = input('Digite o nome do aluno 1: ')
nro2 = input('Digite o nome do Aluno 2: ')
nro3 = input('Digite o nome do Aluno 3: ')
nro4 = input('Digite o nomeo do Aluno 4: ')
#criar uma lista []. Para Python lista fica em conhetes
alunos = [nro1, nro2, nro3, nro4]
#sortear o aluno
sorteado = random.choice(alunos)

print(f'O aluno escolhido é {sorteado}')