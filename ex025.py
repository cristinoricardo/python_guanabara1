#25 Crie um progrma que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
#A função strip() em Python é usada para remover
# espaços em branco (ou outros caracteres especificados) do início e do final de uma string
nome = input("Digite seu nome: ").strip()
#A função upper() em Python é um método de string que converte todos os caracteres de uma string para maiúsculas.
if 'SILVA' in nome.upper():
    print('Tem SILVA')
else:
    print('Não tem!')