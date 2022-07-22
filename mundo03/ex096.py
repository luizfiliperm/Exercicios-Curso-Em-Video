# Faça um programa que tenha uma função chamada área() que receba as dimensões de um terreno retangular (largura e cumprimento) e mostre a área do terreno.

def area(largura, comprimento):
    area = largura * comprimento
    print(f"A área de um terreno {largura}x{comprimento} é {area}m²")


print(f"\n{'Controle de terrenos':^30}")
print('*' * 30)

largura = float(input("LARGURA (m): "))
comprimento = float(input("COMPRIMENTO (m): "))
area(largura,comprimento)