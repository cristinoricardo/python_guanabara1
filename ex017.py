#17 Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
# de um triangulo retângulo, calcule e mosre o comprimento da hipotenusa.
cat_op = float(input('Digite o comprimento do cateto oposto: '))
cat_adj = float(input('Digite o comprimento do cateo adjacene: '))
import math
print('A hipotenusa é: {:.2f}'.format(math.hypot(cat_op, cat_adj)))

#Importar somente o um metodo

from math import hypot
cat_op = float(input('Digite o comprimento do cateto oposto: '))
cat_adj = float(input('Digite o comprimento do cateo adjacene: '))
hi = int(hypot(cat_op, cat_adj)
print(f'A hipotenusa é: {hi}!)