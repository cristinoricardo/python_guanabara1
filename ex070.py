'''70: Crie um programa que leia o nome e o preço de vários produtos.
 O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
 A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.'''

total = 0
prodA = 0
cont = 0
menor = 0
barato = ''

while True:
    produto = str(input('Qual o nome do produto? '))
    preco = float(input('Qual o preço do produto: R$ '))

    total += preco
    cont += 1

    if preco > 1000:
        prodA += 1

    if cont == 1:
        menor = preco
        barato = produto
    else:
        if preco < menor:
            menor = preco
            barato = produto

    resp = ' '
    while resp not in 'SN':  # Evita que o usuario digite outro valor que não seja Sim ou Não.
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break

print(f'O total gasto na compra é R$ {total:.2f}')
print(f'Tem {prodA} produto(s) que custam mais de R$ 1000,00')
print(f'O produto mais barato foi "{barato}" que custa R$ {menor:.2f}')
print('Acabou!')
