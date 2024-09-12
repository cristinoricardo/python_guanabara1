#48 Faça uma progrma que calcule a soma entre todos os números impaes que são múltiplos de três e
# que se encontra
#no intervalo de 1 até 500.

import math
soma = 0 #acumalador
cont = 0 #contador
for c in range(1,501):
    if c%2 != 0:
       if c%3==0:
           cont = cont +1
           soma= soma + c
print('A soma de todos os valores é {}.'.format(soma))
