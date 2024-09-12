#51 Desenvolva um programa que leia o primeiro termo e razão de uma PA. No final,
# mostre os 10 primeiros termos dessa progressão.

primeiro = int(input("Digite o primeiro termo: "))
razao = int(input('Digite a razão: '))
décimo = primeiro + (10-1) * razao
for c in range(primeiro, décimo, razao):
    print('{}'.format(c), end= ' → ')
print('ACABOU')
#atalho da seta é Seta para a direita (→): Pressione Alt + 26
#1: Esse é o primeiro valor especificado na função range().
# Ele define o início do intervalo (ou sequência) de números.
#10: Esse é o segundo valor especificado na função range().
#Ele define o fim do intervalo (ou sequência) de números.
#No entanto, o valor final não é incluído na sequência.
#1: Esse é o terceiro valor especificado na função range().
# Ele define o passo ou incremento entre os números na sequência.
# Nesse caso, estamos incrementando de 1 em 1.


