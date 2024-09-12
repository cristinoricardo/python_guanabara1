#45 Crie um programa que faça o computador jogar Jokenpô com você

from random import randint
print('[0] - Papel')
print('[1] - Tesoura')
print('[2] - Pedra')
user=int(input('Vamos jogar! Escolha um numero: '))
itens = ('Papel', 'Pedra', 'Tesoura')
# faça a lista para ser sorteada

pc=randint(0, 2)
print('O computador escolheu {}!'.format(itens[pc]))
print('Você escolheu {}'.format(itens[user]))
if pc == 0: # PC jogou Papel
    if user == 0:
        print('Você empatou!')
    elif user == 1:
        print('Você Perdeu!')
    elif user == 2:
        print('Você Ganhou!')
elif pc == 1: # PC jogou Tesoura
    if user == 1:
        print('Você empatou!')
    elif user == 0:
        print('Você Perdeu!')
    elif user == 2:
        print('Você Ganhou!')

elif pc == 2: # PC jogou Pedra
    if user == 2:
        print('Você empatou!')
    elif user == 1:
        print('Você Ganhou!')
    elif user == 0:
        print('Você Perdeu!')





