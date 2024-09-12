#39 Faça um programa que leia o ano de nascimento de um jovem e infome de acordo
#com sua idade:
#Se ele ainda vai se alistar ao serviço militar.
#Se é a hora de se alistar
#Se já passou do tempo do alistamento
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo

from datetime import datetime
ano = int(input('Informe o ano de nascimento: '))
ano_atual=datetime.now().year
idade= ano_atual-ano
tempo = 18 - idade
print(f'Sua idade é {idade} anos')
if idade == 18:
    print('É hora de se alistar! ')
elif idade > 18:
    print('Já passou do prazo!')
else:
    print(f'Faltam {tempo} anos para você se alistar')
