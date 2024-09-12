#26 Faça um programa que leia uma frase e mostre:
#a) Quantas vezes aparece a letra "A"
#b) Em que posição aparece a primeira vez.
#c) Em que posição ela aparece a última vez.
nome = str(input('Digite seu nome: '))
nome1 = nome.strip().lower()
print('a) A quantidade de A: ',nome1.count('a'))
print('b) O "A" aparece a primeira vez na posição: ',nome1.find("a")+1)
#rfind, procura começa pelo lado direito
print('c) O "A" aparce a ultima vez na posição: ', nome1.rfind("a")+1)
