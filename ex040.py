#40 Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando
#uma mensagem no final, de acordo com a média atingida:
#- Média abaixo de 5 = REPROVADO
#- Média entre 5.0 e 6.9 = RECUPERAÇÃO
#- Média 7.0 ou superior: APROVADO

nota1= float(input('Escreva sua primeira nota: '))
nota2 = float(input('Escreva sua segunda nota: '))
media = (nota1+nota2)/2
print(f'Sua média é {media}')

if media >= 7.0:
    print('Voê foi aprovado!')
elif  7> media >= 5:
    print('Você está de RECUPERAÇÃO!')
else:
    print('Você foi REPROVADO!')
