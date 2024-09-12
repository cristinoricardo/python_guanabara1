#37 [Base númericos] Escrea um programa que leia um número inteiro qualquer e peça
# o usuário escolher qual será a base de conversão:
#1 para binario
#2 para octal
#3 para hexadecimal

num=int(input('Digite um numero: '))
print('''Escolha uma das bases para conversão:
[1] Binário
[2] OCTAL
[3] HEXADECIMAL''')
opcão = int(input('Sua opção: '))
if opcão==1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num,bin(num)[2:])) # [:2] é o fatiamento
#para aparecer somente a partir do segundo digito.
elif opcão==2:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, oct(num)[2:]))
elif opcão == 3:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Valor invalido')