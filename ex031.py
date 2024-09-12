#31 Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem
#cobrando R$ 0,50 por km para viagens de até 200km e R$ 0,45 para viagens mais longas.

dist = float(input('Digite a distância: '))
if dist < 200:
    cal1 = dist * 0.50
    print('O valor da passagem é R$ {:.2f}.'.format(cal1))
else:
    cal2 = dist * 0.45
    print('O valor da passagem é R$ {:.2f}.'.format(cal2))