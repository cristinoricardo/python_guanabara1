#32 Faça um programa que leia um ano qualquer e mostre se ele é bissexto
from datetime import date
ano = int(input('Digite um ano: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: # != é usando para falar que é "DIFERENTE"
    print('O {} é BISSEXTO'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO'.format(ano))