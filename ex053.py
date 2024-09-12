#53 Crie um progrma que leia uma frase qualque e diga se ela é  um palindromo,
# desconsiderando os espaços.

frase = str(input('Digite uma frase: ')).upper().strip()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('É um palídromo!')
else:
    print('Não é um palídromo!')

