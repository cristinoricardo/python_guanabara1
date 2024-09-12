'''059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''

nro1 = int(input('Digite o primeiro número: '))
nro2 = int(input('Digite o segundo número: '))
opcao = 0
while opcao != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opcao = int(input('Qual é a sua opção? '))
    if opcao == 1:
        soma = nro1 + nro2
        print("A soma é {}.".format(soma))
    elif opcao == 2:
        produto =  nro1 * nro2
        print("A multiplicaçã é {}.".format(produto))
    elif opcao == 3:
        if nro1 > nro2:
            maior = nro1
        else:
            maior = nro2
            print('O número maior é {}.'.format(maior))
    elif opcao == 4:
        print('Informe o número novamente!')
        nro1 = int(input('Digite o primeiro número: '))
        nro2 = int(input('Digite o segundo número: '))
    else:
        print('Opção inválida. Tente novamente!')

print('Fim do programa!Até logo...')