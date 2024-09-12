'''# 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar"
 em um número entre 0 e 10. Só que agora o jogador vai tentar
adivinhar até acertar, mostrando no final quantos palpites
 foram necessários para vencer.'''

import random

palpite = 0 #acumalador
computador = random.randint(0,10) #Randit sorteia um numero
acertou = False #O jogador não deu nenhum palpite, logo não acertou
while not acertou: #Enquanto o jogador não acertar ele vai fazer a condição abaixo.
    nro = int(input('Digite um numero de 0 a 10: '))# primeira vez que o jogador dar um palpite
    palpite += 1 #soma os palpites do jogador
    if nro == computador: #se  ele acertar será verdadeiro
        acertou = True
    else:
        if nro < computador:
            print('Mais... Tente novamente: ')
        elif nro > computador:
            print('Menos... Tente novamente: ')
print('Você acertou com {} tentativas!'.format(palpite))
