#43 Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule seu
#IMC e mostre seu status, de acordo com a tabela abaixo:
#-Abaixo 18.5: Abaixo do peso
#- Entre 18.5 e 25: Peso ideal
#- 25 até 30: Sobrepeso
#- 30 até 40: Obesidade
#- Acima de 40: Obesidade mórbida

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc= (peso/(altura**2))
print(f'Seu IMC é {imc:.2f}')

if imc<18.5:
    print('Você está abaixo de peso!')
elif imc <25:
    print('Você está no Peso Ideal')
elif imc<30:
    print('Você está com sobrepeso!')
elif 30<=imc<40:
    print('Você está Obeso')
else:
    print('Você esta com Obesidade Mórbida!')

