#29 Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele multado
#A multa vai custar R$ 7,00 por cada km acima do limite

# Solicita ao usuário que insira a velocidade do carro
vel = int(input('Escreva a velocidade do carro: '))
# Verifica se a velocidade é maior que 80
if vel > 80:
    # Calcula a multa
    multa = (vel-80)*7
    # Imprime a mensagem de multa e o valor da multa
    print('Você foi multado!')
    print('O valor da multa é: R$ {:.2f}'.format(multa))
else:
    # Informa que a velocidade está dentro do limite
    print('Muito bem. Você está no limite.')

