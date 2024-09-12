#30 Crie um progrma que leia um numero inteiro e mostre na telase ele é PAR ou Ímpar
nro = int(input('Digite um número: '))

#Se o resto da divisão de um número por 2 for 0, então o número é par; caso contrário, ele é ímpar.
if nro % 2 == 0:
    print('É par')
else:
    print('É impar!')