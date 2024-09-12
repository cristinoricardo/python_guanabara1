#18 Faça um programa que leia um ângulo
# qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo
import math
ang = float(input('Digite o valor de um angulo: '))
#O angulo tem que ser em radiano e não em graus
print('O seno é: {:.2f}'.format(math.sin(math.radians(ang))))
print('O consseno é: {:.2f}'.format(math.cos(math.radians(ang))))
print('A tangente é: {:.2f}'.format(math.tan(math.radians(ang))))