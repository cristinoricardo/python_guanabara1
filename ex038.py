#38 Escreva um programa que leia dois números inteiroos e compare-os, mostrando na tela
#uma mensagem:
#O primeiro valor é maior
#O segundo valor é maior
#Não existe valor maior, os dois são iguais

nro1 = int(input('Escreva o número 1: '))
nro2 = int(input('Escreva o número 2: '))

if nro1 > nro2:
    print(' Número 1 maior que número 2')
elif nro2 > nro1:
    print('Número 2 maior que número 1')
else:
    print('Não existe valor maior, os dois são iguais.')
