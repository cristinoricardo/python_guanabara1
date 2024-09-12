'''Crie um programa que leia vários números inteiros pelo teclado.
 No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''

resp = 'S'
soma = 0
quant = 0
media = 0
maior = 0
menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma = soma + num
    quant = quant + 1
    if quant == 1: #Neste caso foi digitado somente um número
            menor = maior = num
    else:
        if num > maior:
            menor = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
média = soma/ quant
print('Você digitou {} números e a média foi {}'.format(num, média))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))