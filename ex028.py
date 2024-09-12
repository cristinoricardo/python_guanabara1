#28 Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e
# peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
import random

nro = int(input('Escreva um número de 0 e 5: '))
computador = random.randint(0,5) #Randit sorteia um numero.
print('O computador escolheu {}'.format(computador))

if nro == computador:
    print('Você venceu!')
else:
    print('O computador venceu!')

