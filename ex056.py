#56 Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do program mostre:
# A média de idade do grupo
#Qual é o nome do homem mais velho.
#Quantas mulheres tem menos de 20 anos.

somaidade = 0
mediaidade = 0 #contador
maioridadehomem = 0
nomevelho = ' '
totalmulher20 = 0
for p in range(1, 5):
    print ('____{}º PESSOA _____'.format(p))
    nome = str(input('Nome: ')).strip() #remover o espaço em branco
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in "Mm": #o in segnifica se for ou outro
        maioridadehomem = idade
        nomevelho = nome
    if sexo in "Mm" and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in "Ff" and idade < 20:
        totalmulher20 += 1

mediaidade = somaidade / 4
print('A média de idade do grupo é de {} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {} '.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos. '.format(totalmulher20))

