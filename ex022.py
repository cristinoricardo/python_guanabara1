#22 Crie um programa que leia o nome completo de um pessoa e mostra:
#a) O nome com todas as letras maiusculas
#b) O nome com todas minusculas
#c) Quantas letras ao todo (sem considerar os espaços)
#d) Quantas letras tem o primeiro nome

nome = str(input('Digite o nome: ')),strip()
print('A)  Colocar o nome com todas as letras maiusculas',nome.upper())
print('B) Colocar o nome com todas as letras minusculas',nome.lower())
total_letras = len(nome.replace(" ", ""))
print('C) Quantas letras ao todo (sem considerar os espaços):', total_letras)
primeiro_nome = nome.split()[0]
print('D) Quantas letras tem o primeiro nome:', len(primeiro_nome))
#split separar os nomes em listas
segundo_nome = nome.split()[1]
print('E) A quantidade de letras do segundo nome é: ',len(segundo_nome))
