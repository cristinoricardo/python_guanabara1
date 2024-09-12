#41 A confederação de Natação precisa de um programa que leia o ano de nascimento
#de um atleta e mostre sua categoria, de acordo com a idade:
#- Até 9 anos: Mirim
#- Até 14 ANos: INFANTIL
#-  Até 19 anos:  Junior
#- Até 20 anos = Sênior
#- Acima de 20 = MASTER

from datetime import datetime
ano = int(input('Escreva o ano que você nasceu: '))
ano_atual = datetime.now().year
#Now() é atual, agora
idade = ano_atual-ano

print(f'Sua idade é {idade}')

if idade < 9:
    print('Categoria MIRIM')
elif idade < 14:
    print('Infantil')
elif idade < 19:
    print('Junior')
elif idade < 20:
    print('Sênior')
else:
    print('Master')
