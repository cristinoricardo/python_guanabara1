#35 Desenvolva uma programa que leia o comprimento de
# três retas e diga ao usuários se elas podem ou não formar um triângulo.
import time
print('-='*20)
print('Analisador de Triangulos..')

a = int(input('Digite o valor de uma reta 1: '))
b = int(input('Digite o valor de uma reta 2 : '))
c = int(input('Digite o valor de uma reta 3: '))

print('Analisando as retas..')
time.sleep(2)
if (a+b) < c or (b+c) < a or (c+a) < b:
    print('\033[0;30;45mPode ser um triangulo!\033[m') #\033[0:30:40m é usando para colorir no terminal
else:
    print('\033[0;30;45mNão pode ser um triangulo!\033[m')