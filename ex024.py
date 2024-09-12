#24 Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"
#O método strip() em Python é usado para remover espaços em branco do início e do final de uma string.
# Isso inclui espaços, tabs, quebras de linha e outros caracteres de espaço.

#coloquei strip no final do codigo para tirar os espaço do começo
cidade = str(input("Digite o nome de uma cidade: ")).strip()
#coloque dois pontos no final da linha "if"
if cidade[:5].upper()== "SANTO":
# 4 espaços no começo para colocar a linha dentro do codigo if (Indetação)
    print("Tem")
else:
    print('Não tem!')


