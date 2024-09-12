#33 Faça um programa que leia trés números e mostre qual é o maior e qual é o menor.
nro1 = int(input('Digite um numero 1: '))
nro2 = int(input('Digite o numero 2: '))
nro3 = int(input('Digite o numero 3: '))
#elif é um condição que caso seja verdadeira a condição é executado, caso contrario ela vai para proxima codição.
if nro1 > nro2 and nro1 > nro3:
    maior = nro1
    print('O {} é o maior!'.format(maior))
elif nro2 >nro1 and nro2>nro3:
    maior  = nro2
    print('O {} é o maior!'.format(maior))
else:
    print('O maior é {}'.format(nro3))

if nro1 < nro2 and nro1 < nro3:
    menor = nro1
    print('O {} é o menor!'.format(menor))
elif nro2 < nro1 and nro2 < nro3:
    menor = nro2
    print('O {} é o menor!'.format(menor))
else:
    print('O menor é {}'.format(nro3))