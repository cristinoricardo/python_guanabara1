'''67: Faça um programa que mostre a tabuada de vários números,
 um de cada vez, para cada valor digitado pelo usuário.
 O programa será interrompido quando o número solicitado for negativo.'''


while True:
    num = int(input('Qual o numero quer a tabuada?'))
    if num <= 0:
        break
    for n in range(1,11):
        print (f'{num} x {n} = {num*n:2}')
print(('Tabuada encerrada!'))

