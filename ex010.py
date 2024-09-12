#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar. U$$ = R$ 3,27
reais = float(input("Quantos você tem em reais?"))
#No python a casa decimal é separada por ponto [.]
cotacao_do_dolar = float(input("Qual o valor do dolar hoje?"))
div = reais / cotacao_do_dolar
#Lembre de colocar o ponto [.]  antes de format
print("Em dolares você tem {:.2f}.".format(div))

import requests
url = 'https://economia.awesomeapi.com.br/all/USD-BRL'
response = requests.get(url)

if response.status_code == 200:
    moeda_valor = response.json()['USD']['high']
    print("A cotação do dólar é {}!".format(moeda_valor))
else:
    print("Erro na verificação da cotação!")