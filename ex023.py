#23 Faça um progrma que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
#Unidade
#Dezena
#Centena
#Milhar

nro = int((input('Digite um numero de 0 a 9999:')))
u = nro // 1 % 10
d = nro // 10 % 10
c = nro // 100 % 10
m = nro // 1000 % 10
#primeiro nro é milhar, segundo é centena, terceiro é dezena e quarto é unidade

print('Unidade é: {}'.format(u))
print('Dezena é: {}'.format(d))
print('Centena é: {}'.format(c))
print('Milhar é: {}'.format(m))

