#44 Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu
#preço normal e condição de pagamento:
#- À vista dinheiro / cheque: 10% de desconto
#- À vista no cartão: 5% de desconto
#- em até 2x no cartão: preço normal
#- 3x ou mais no cartão: 20% de juroS

print('{:=^40}'.format('LOJAS GUANABARA')) # {:=^40} ESSA CONDIÇÃO ALINHA NO CENTRO

produto=float(input('Digite o valor do produto R$: '))
print('1- À vista')
print('2- Cheque')
print('3- Cartão 1 vez')
print('4- Cartão 2 vezes')
print('5- Cartão 3 vezes')
forma= int(input('Digite o número da forma de pagamento: '))


if forma== 1:
    preco=produto*0.90
    print(f'O preço com 10% de desconto é R$ {preco:.2f}')
elif forma==2:
    preco=produto*0.90
    print(f'O preço com 10% de desconto é R$ {preco:.2f}')
elif forma==3:
    preco = produto * 0.95
    print(f'O preço com 5% de desconto é R$ {preco:.2f}')
elif forma==4:
    preco=produto
    print(f'O preço é R$ {preco:.2f}')
else:
    preco = produto*1.20
    print(f'O preço é R$ {preco:.2f}')