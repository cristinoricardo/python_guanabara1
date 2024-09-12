##Faça uma algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.
salario = float(input(("QUal o seu salário atual?")))
aument = float(input("Qual o valor de aumento?"))
aumento = salario+(salario *aument/100)
print("O salário com aumento de {}% é {}".format(aument,aumento))
