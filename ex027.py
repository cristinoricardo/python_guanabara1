## 27 Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o ultimo nome separadamente

n=str(input('Digite seu nome completo:')).strip()
#divida em lista
nome =n.split()
print('Muito prazer em te conhcer!')
print('Seu primeiro nome é:{} '.format(nome[0]))
#Dentro [] é a condição da lista
print('Seu ultimo nome é {}'.format(nome[len(nome)-1]))
