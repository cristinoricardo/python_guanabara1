#50 Desenvol uma progrma que leia seis números inteiros e mostre soma apenas daqueles que
# forem pares. Se o valor digitado for ímpar desconsidere-o.

soma = 0
cont = 0 #soma
for c in range(1,7):
    num = int(input("Digite o  valor do {} numero: ".format(c)))
    if num % 2 == 0: #numeros pares
        cont = cont + 1 #contador
        soma = soma + num #soma += num - acumalador

print('A soma dos {} números pares é igual a {}'.format(cont, soma))
