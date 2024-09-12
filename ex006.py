#Desafio 6 = Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada
#Para calcular a raiz quadrada coloque a potenciazação (**) por 1/2
n1 = float(input('Digite um numero'))
print('O dobro é {}' .format(n1*2))
print('O triplo é {}'.format(n1*3))
#A função pow() é uma função integrada do Python que é usada para calcular potências. Ela pode ser chamada de duas formas:

#pow(x, y) - Calcula x elevado à potência y.
#pow(x, y, z) - Calcula (x**y) % z, o que é útil para operações modulares em criptografia e outras áreas.

print("A raiz quadrada {}".format((n1**(1/2))))
