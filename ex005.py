#Desafio 5 - Faça um programa que leia um número inteiro e mostre na tela o seu sucesso e seu antecessor
#Para usar a máscara {} não use a virgula antes de .format
n1 = int(input("Digite um numero"))
ant = n1 - 1
suces = n1 + 1
print("O antecessor é {} e o suecessor é {}".format(ant,suces))
#coloque f para preencher os conchetes das máscaras.
print(f"O antecessor {ant} e o sucessor é {suces}")
