#42 Refaça o Desafio 035 dos triângulos, acrescentando o recusso de mostrar
#que tipo de triângulo será formado:
#- Equilatero : Todos os lados igauis
#- Isósceles = Dois lados iguais
#- Escaleno -  Todos os lados diferentes

import time
print('-='*20)
print('Analisador de Triangulos..')

a = int(input('Digite o valor de uma reta 1: '))
b = int(input('Digite o valor de uma reta 2 : '))
c = int(input('Digite o valor de uma reta 3: '))

print('Analisando as retas..')
#time.sleep(2)
# para usar diferente {!=}

if (a+b) < c or (b+c) < a or (c+a) < b or a==b==c:
    print('\033[0;30;45mPode ser um triangulo!\033[m') #\033[0:30:40m é usando para colorir no terminal
    if a == b == c:
        tipo = 'Equilátero'
    elif a == b or b == c or c == a:
        tipo = 'Isósceles'
    else:
        tipo = 'Escaleno'
    print(f'Pode ser um triângulo {tipo}')
else:
    print('\033[0;30;45mNão pode ser um triangulo!\033[m')

