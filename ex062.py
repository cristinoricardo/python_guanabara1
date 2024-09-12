'''62: Melhore o DESAFIO 061, perguntando para o
usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos.'''

primeiro = int(input("Digite o primeiro termo: "))
razao = int(input('Digite a razão: '))
termo = primeiro
cont = 1 #usar um porque é uma soma que começa com um
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} → '.format(termo), end='')
        termo += razao
        cont +=1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão com {} termos mostrados.'.format(total))
print('ACABOU')
