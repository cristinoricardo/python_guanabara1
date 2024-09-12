#36 Escreva um progrma para aprovar o empréstimo bancário para
#comprar de uma casa. O programa vai perguntar o valor da casa, o salário
#do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode
#exceder 30% do salário oou então o empréstino será reprovador.

casa=float(input('Qual o valor da casa? R$: ')) #Use float pois o valor pode ter casa decimais
sal=float(input('Qual o seu salário? R$: '))
prazo=int(input('Qual o prazo anual? : '))

mes= prazo*12
prest=casa/mes
prest1 = round(prest,2)
lmt_p=sal*(30/100)
print('O prazo mensal são {} meses'.format(mes))
print('A parcela mensal é R$ {} e '.format(prest1), end='') #o end é para continuar
print('O valor máximo da parcela é R$ {}'.format(lmt_p))

if lmt_p >= prest:
    print('Financiamento aprovado!')
else:
    print('Financiamento reprovado!')