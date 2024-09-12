#20 O professor quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

n1 = str(input(("Digite o numero do aluno 1:  ")))
n2 = str(input(('Digite o nome do aluno 2: ')))
n3 = str(input(('Digite o nome do aluno 3: ')))
n4 = str(input(('Digite o nome do aluno4: ')))
#CRIAR UMA LISTA
lista = [n1, n2, n3, n4]
#USAR O COMANDO shuffle para embaralhar
random.shuffle(lista)
print('A ordem de alunos é' )
print(lista)