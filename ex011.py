#Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade de tinta necessária para pinta-la, sabendo que cada litro de tinta, pinta um área de 2 metros quadrados.
larg = float(input("Qual a largura da sua parede?"))
alt = float(input("Qual a altura da sua parede?"))
area = float(larg*alt)
tinta = float(area/2)
print(f"A area de sua parede é {area}")
print(f"Você vai precisar de {tinta} latas de tintas para pintar a parede")
