#34 Escreva um progrma que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$ 1.250,00 calcule um aumento de 10%. Para inferiores  ou iguais aumento de 15%
sal = int(input('Digite o valor do seu sálario:R$ '))
if sal >= 1250:
#Use o nome da variante igual
    aumento = sal * 0.10
    print('O aumento será de {}'.format(aumento))
else:
    aumento = sal * 0.15
    print('O aumento será de {}'.format(aumento))