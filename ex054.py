#54 Crie um programa que leia o ano de nascimento de sete pessoas. No final mostre quantas
# pessoas ainda não atingiram a maoriodade (>20 anos) e quantas já são maiores.

from datetime import datetime
atual = datetime.today().year
totmaior = 0
totmenor = 0
for pess in range(1,8):
    nasc = int(input('Em que ano a {}º a pessoa nasceu? '.format(pess)))
    idade = atual - nasc
    if idade >= 21:
        totmaior +=1
    else:
        totmenor += 1
print('Tem {} maior de idade.'.format(totmaior))
print('Tem {} menor de idade.'.format(totmenor))
